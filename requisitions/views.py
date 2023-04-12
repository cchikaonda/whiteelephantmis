from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render,redirect, get_object_or_404
from inventory.models import *
from django.template.loader import render_to_string

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.db.models import AutoField,IntegerField,FloatField,ExpressionWrapper, F, DecimalField, Count, Sum
from djmoney.money import Money
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.db.models.functions import Lower
from djmoney.models.fields import MoneyField
from .forms import SearchForm
from .models import *
from basket.basket import Basket

@login_required
def requisitions_list(request):
    if request.user.has_perm('can_view_all_requisitions'):
        requisitions = Requisition.objects.all()
        approved_requisitions = requisitions.filter(status = 'Approved')
        pending_requisitions = requisitions.filter(status = 'Pending')
        denied_requisitions = requisitions.filter(status = 'Denied')

    else:
        requisitions = Requisition.objects.filter(user=request.user)
        approved_requisitions = requisitions.filter(status = 'Approved')
        pending_requisitions = requisitions.filter(status = 'Pending')
        denied_requisitions = requisitions.filter(status = 'Denied')
    context = {
        'header':'Manage Requisitions',
        'requisitions':requisitions,
        'approved_requisitions':approved_requisitions,
        'pending_requisitions':pending_requisitions,
        'denied_requisitions':denied_requisitions,
    }
    return render(request, 'requisitions/requisitions_list.html', context)

@login_required
def create_requisition(request):
    item_search_form = SearchForm()
    items = Item.objects.all()
    item_categories = ItemCategory.objects.all()
    items = None
    item_cat_id = request.GET.get('category')
    if item_cat_id:
        items = Item.get_all_items_by_category_id(item_cat_id).filter(active=True).filter(quantity_at_hand__gt=0)
        item_count = items.count()
    else:
        items = Item.get_all_items().filter(active=True).filter(quantity_at_hand__gt=0)
        item_count = items.count()
    all_items_count = Item.objects.count()
    category = ItemCategory.objects.filter(id=item_cat_id)
    context = {
        'header':'Create Requisition',
        'item_categories':item_categories,
        'category':category,
        'items':items,
        'all_items_count':all_items_count,
        'item_count':item_count,
        'item_search_form':item_search_form,
    }
    return render(request, 'requisitions/create_requisition.html', context)

@login_required
def edit_requisition(request, id):
    item_search_form = SearchForm()
    items = Item.objects.all()
    item_categories = ItemCategory.objects.all()
    requisition = Requisition.objects.get(id = id)
    request.session['opened_requisition'] = requisition.id
    items = None
    item_cat_id = request.GET.get('category')
    if item_cat_id:
        items = Item.get_all_items_by_category_id(item_cat_id).filter(active=True).filter(quantity_at_hand__gt=0)
        item_count = items.count()
    else:
        items = Item.get_all_items().filter(active=True).filter(quantity_at_hand__gt=0)
        item_count = items.count()
    all_items_count = Item.objects.count()
    category = ItemCategory.objects.filter(id=item_cat_id)
    context = {
        'header':'Edit Requisition',
        'item_categories':item_categories,
        'category':category,
        'items':items,
        'requisition':requisition,
        'all_items_count':all_items_count,
        'item_count':item_count,
        'item_search_form':item_search_form,
    }
    return render(request, 'requisitions/edit_requisition.html', context)

@login_required
def remove_single_item_from_cart(request, slug):
    request_id =request.session['opened_requisition']
    item = get_object_or_404(Item, slug=slug)
    req_qs = Requisition.objects.filter(id = request_id)
    if req_qs.exists():
        requisition = req_qs[0]
        req_code = Requisition.objects.get(id = request_id).get_code()
        #check if the requested item is in the request
        if requisition.items.filter(item__slug = item.slug).exists():
            requested_item = RequestItem.objects.get(item=item, request_id = req_code )
            if requested_item.approved_qty > 0:
                requested_item.approved_qty -=1
                item.quantity_at_hand +=1
                requested_item.save()
                item.save()
            return redirect('/edit_requisition/'+ str(request_id))
        else:
            return redirect('/edit_requisition/'+ str(request_id))
    else:
        messages.info(request, "Item not in order")
    # return redirect('/pos/personal_order_list/'+ str(order.id))
    return redirect('/edit_requisition/'+ str(request_id))

@login_required
def add_single_item_from_cart(request, slug):
    request_id =request.session['opened_requisition']
    item = get_object_or_404(Item, slug=slug)
    req_qs = Requisition.objects.filter(id = request_id)
    if req_qs.exists():
        requisition = req_qs[0]
        req_code = Requisition.objects.get(id = request_id).get_code()
        #check if the requested item is in the request
        if requisition.items.filter(item__slug = item.slug).exists():
            requested_item = RequestItem.objects.get(item=item, request_id = req_code )
            if requested_item.item.quantity_at_hand > 0:
                requested_item.approved_qty +=1
                item.quantity_at_hand -=1
                requested_item.save()
                item.save()
            return redirect('/edit_requisition/'+ str(request_id))
        else:
            return redirect('/edit_requisition/'+ str(request_id))
    else:
        messages.info(request, "Item not in order")
    return redirect('/edit_requisition/'+ str(request_id))

#item details view
def item_details(request, id):
    item = get_object_or_404(Item, id = id)
    context = {
        'item':item,
        'title':'IMIS',
        'header': 'Item details',
    }
    return render(request, 'item_details.html', context)

#submit request
def submit_requisition(request):
    basket = Basket(request)
    if request.user.is_authenticated:
        request_total_cost =  basket.get_total_price()
        session = request.session
        req = Requisition.objects.create(user = request.user, request_total_cost = request_total_cost)
        req.code = req.get_code()
        req.save()
        req_id = req.get_code()
        for item in basket:   
            requested_item = RequestItem.objects.create(
                request_id=req_id, item =item["item"], requested_item_price=item["price"], quantity=item["qty"], approved_qty = item["qty"],
            )
            req.items.add(requested_item)
            req.save()
        messages.success(request, "Request Successfully submitted!")
        del request.session['basket']
        return redirect('requisitions_list')

def approve_requisition(request, id):
    requisition = Requisition.objects.get(id = id)
    req_id = requisition.get_code()
    requested_items = RequestItem.objects.filter(request_id = req_id)
    for requested_item in requested_items:
        item = Item.objects.get(item_name = requested_item.item)
        item.quantity_at_hand = requested_item.get_item_balance()
        item.save()
        requested_item.approved = True
        requested_item.save()
    requisition.status = "Approved"
    requisition.approved_by = request.user
    requisition.save()
    messages.success(request, "Request Successfully Approved!")
    return redirect('requisitions_list')

def deny_requisition(request, id):
    requisition = Requisition.objects.get(id = id)
    req_id = requisition.get_code()
    # requested_items = RequestItem.objects.filter(request_id = req_id)
    # for requested_item in requested_items:
    #     item = Item.objects.get(item_name = requested_item.item)
    #     item.quantity_at_hand = requested_item.get_item_balance()
    #     item.save()
    #     requested_item.approved = True
    #     requested_item.save()
    requisition.status = "Denied"
    requisition.approved_by = request.user
    requisition.save()
    messages.success(request, "Request Denied!")
    return redirect('requisitions_list')


def basket_clear(request):
    basket = Basket(request)
    print(basket)
    basket.clear()
    print(basket)
    return redirect ('create_requisition')

