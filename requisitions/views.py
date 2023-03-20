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

@login_required
def requisitions_list(request):
    context = {
        'header':'Manage Requisitions'
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

#item details view
def item_details(request, id):
    item = get_object_or_404(Item, id = id)
    context = {
        'item':item,
        'title':'IMIS',
        'header': 'Item details',
    }
    return render(request, 'item_details.html', context)
