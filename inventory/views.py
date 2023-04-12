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
from inventory.forms import AddCategoryForm, AddItemForm, AddUnitForm, AddSupplierForm, AddBatchForm, AddStockForm
from inventory.models import *
from requisitions.models import *
from inventory.homeChartsData import get_requests_last_week, get_requests_this_week

# Inventory dashboard page.
def get_total_items_percategory(category, requested_items):
    requested_items = requested_items.filter(item__category = category)
    total_items = 0
    if requested_items != None:
        for requested_item in requested_items:
            total_items += requested_item.quantity
        print(total_items)
    return total_items

@login_required
def home(request):
    item_categories = ItemCategory.objects.all()
    total_req_items_per_cat_lw = []
    total_req_items_per_cat_tw = []

    requests_tw = get_requests_this_week()
    requests_lw = get_requests_last_week()

    for item_cat in item_categories:
        dicttw = {}
        dicttw['category'] = item_cat.category_name
        dicttw['total'] = get_total_items_percategory(item_cat, requests_tw)
        total_req_items_per_cat_tw.append(dicttw)

        dictlw = {}
        dictlw['category'] = item_cat.category_name
        dictlw['total'] = get_total_items_percategory(item_cat, requests_lw)
        total_req_items_per_cat_lw.append(dictlw)
    # total_req_items_per_cat = sorted(total_req_items_per_cat, key=lambda x:x['total'], reverse=True)
    items_run_out_of_stock = get_items_running_out_of_stock()
    context = {
        'items_run_out_of_stock':items_run_out_of_stock,
        'total_req_items_per_cat_lw':total_req_items_per_cat_lw,
        'total_req_items_per_cat_tw':total_req_items_per_cat_tw,

    }
    return render(request, 'home.html', context)

#Items running out of stock
def get_items_running_out_of_stock():
    return Item.objects.filter(quantity_at_hand__lte = F('reorder_level'))

@login_required
def item_list(request):
    items = Item.get_all_items()

    expected_sum_items_cost = 0
    for item in items:
        expected_sum_items_cost += item.get_expected_revenue()

    item_cats = ItemCategory.get_all_item_categories()
    item_cat_id = request.GET.get('category')
    
    if item_cat_id != None:
        items = Item.get_all_items_by_category_id(item_cat_id)
    context = {
        'items': items,
        'header': 'Manage Items',
        'item_cats': item_cats,
        'expected_sum_items_cost':expected_sum_items_cost,
    }
    return render(request, 'items/items_list.html', context)

@login_required
def save_all_items(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items =  Item.objects.all()
            data['item_list'] = render_to_string('includes/items/items_list_2.html',{'items': items,})
    
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
@login_required
@permission_required({("inventory.view_item"),("inventory.can_add_new_item")})
def item_create(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
    else:
        form = AddItemForm()
    return save_all_items(request, form, 'items/item_create.html')

@login_required
def item_update(request, id):
    product = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = AddItemForm(request.POST, instance=product)
    else:
        form = AddItemForm(instance=product)
    return save_all_items(request, form, 'items/item_update.html')

@login_required
def item_delete(request, id):
    data = dict()
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        data['form_is_valid'] = True
        items = Item.objects.all()
        data['item_list'] = render_to_string('items/item_list_2.html', {'items': items})
    else:
        context = {'item': item}
        data['html_form'] = render_to_string('items/item_delete.html', context, request=request)
    return JsonResponse(data)




@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers,
        'header': 'Manage Suppliers',
    }
    return render(request, 'suppliers/supplier_list.html', context)

@login_required
def save_all_suppliers(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            suppliers =  Supplier.objects.all()
            data['supplier_list'] = render_to_string('suppliers/supplier_list_2.html',{'suppliers': suppliers,})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = AddSupplierForm(request.POST)
    else:
        form = AddSupplierForm()
    return save_all_suppliers(request, form, 'suppliers/supplier_create.html')

@login_required
def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == 'POST':
        form = AddSupplierForm(request.POST, instance=supplier)
    else:
        form = AddSupplierForm(instance=supplier)
    return save_all_suppliers(request, form, 'suppliers/supplier_update.html')

@login_required
def supplier_delete(request, id):
    data = dict()
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == "POST":
        supplier.delete()
        data['form_is_valid'] = True
        suppliers = Supplier.objects.all()
        data['supplier_list'] = render_to_string('includes/suppliers/supplier_list_2.html', {'suppliers': suppliers})
    else:
        context = {'supplier': supplier}
        data['html_form'] = render_to_string('suppliers/supplier_delete.html', context, request=request)
    return JsonResponse(data)
@login_required
def category_list(request):
    items = Item.objects.all().order_by('item_name')
    item_cats = ItemCategory.objects.all().order_by('category_name')
    context = {
        'items': items,
        'header': 'Manage Item Categories',
        'item_cats': item_cats,
    }
    return render(request, 'categories/category_list.html', context)

@login_required
def save_all_categories(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            item_cats = ItemCategory.objects.all()
            data['category_list'] = render_to_string('includes/categories/category_list_2.html',{'item_cats': item_cats})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
@permission_required({("inventory.view_itemcategory"),("inventory.can_add_new_category")})
def category_create(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
    else:
        form = AddCategoryForm()
    return save_all_categories(request, form, 'categories/category_create.html')

@login_required
@permission_required({("inventory.view_itemcategory"),("inventory.can_update_category")})
def category_update(request, id):
    category = get_object_or_404(ItemCategory, id=id)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
    else:
        form = AddCategoryForm(instance=category)
    return save_all_categories(request, form, 'categories/category_update.html')


@login_required
def category_delete(request, id):
    data = dict()
    category = get_object_or_404(ItemCategory, id=id)
    if request.method == "POST":
        category.delete()
        data['form_is_valid'] = True
        item_cats = ItemCategory.objects.all()
        data['category_list'] = render_to_string('includes/categories/category_list_2.html',{'item_cats': item_cats})
    else:
        context = {'category': category}
        data['html_form'] = render_to_string('categories/category_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def unit_list(request):
    units = Unit.objects.all().order_by('unit_description')
    context = {
        'header': 'Manage Item Units',
        'units': units,
    }
    return render(request, 'units/unit_list.html', context)

@login_required
def save_unit_list(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            units = Unit.objects.all().order_by('unit_description')
            data['unit_list'] = render_to_string('includes/units/unit_list_2.html', {'units': units})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
@permission_required({("inventory.view_unit"),("inventory.can_add_new_unit")})
def unit_create(request):
    if request.method == 'POST':
        form = AddUnitForm(request.POST)
    else:
        form = AddUnitForm()
    return save_unit_list(request, form, 'units/unit_create.html')

@login_required
def unit_update(request, id):
    unit = get_object_or_404(Unit, id=id)
    if request.method == 'POST':
        form = AddUnitForm(request.POST, instance=unit)
    else:
        form = AddUnitForm(instance=unit)
    return save_unit_list(request, form, 'units/unit_update.html')

@login_required
def unit_delete(request, id):
    data = dict()
    unit = get_object_or_404(Unit, id=id)
    if request.method == "POST":
        unit.delete()
        data['form_is_valid'] = True
        units = Unit.objects.all()
        data['unit_list'] = render_to_string('units/unit_list_2.html', {'units': units})
    else:
        context = {'unit': unit}
        data['html_form'] = render_to_string('units/unit_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def user_list(request):
    pass

@login_required
def save_all_users(request,form,template_name):
	pass

@login_required
def user_create(request):
	pass

@login_required
def user_update(request,id):
	pass

@login_required
def user_delete(request,id):
	pass

@login_required
def user_profile(request):
    pass

@login_required
def change_password(request):
    pass


@login_required
def customer_list(request):
    pass

@login_required
def save_customer_list(request, form, template_name):
    pass

@login_required
def customer_create(request):
    pass

@login_required
def customer_update(request, id):
    pass

@login_required
def customer_delete(request, id):
    pass


@login_required
def batch_list(request):
    batch_numbers = BatchNumber.objects.all()
    stocks = Stock.objects.all()
    context = {
        'stocks':stocks,
        'batch_numbers': batch_numbers,
        'header': 'Manage Batch Numbers',
    }
    return render(request, 'batches/batch_list.html', context)

@login_required
def save_all_batches(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            batch_numbers = BatchNumber.objects.all()
            data['batch_list'] = render_to_string('includes/batches/batch_list_2.html',{'batch_numbers': batch_numbers})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def batch_create(request):
    if request.method == 'POST':
        form = AddBatchForm(request.POST)
    else:
        form = AddBatchForm()
    return save_all_categories(request, form, 'batches/batch_create.html')

@login_required
def batch_update(request, id):
    batch = get_object_or_404(BatchNumber, id=id)
    if request.method == 'POST':
        form = AddBatchForm(request.POST, instance=batch)
    else:
        form = AddBatchForm(instance=batch)
    return save_all_batches(request, form, 'batches/batch_update.html')

@login_required
def batch_delete(request, id):
    data = dict()
    batch = get_object_or_404(BatchNumber, id=id)
    if request.method == "POST":
        batch.delete()
        data['form_is_valid'] = True
        batches = BatchNumber.objects.all()
        data['batch_list'] = render_to_string('batches/batch_list_2.html',{'batches': batches})
    else:
        context = {'batch': batch}
        data['html_form'] = render_to_string('batches/batch_delete.html', context, request=request)
    return JsonResponse(data)

def view_batch_details(request, batch_id):
    stock_items = Stock.objects.filter(batch=batch_id)
    pass


@login_required
def stock_list(request):
    stocks = Stock.objects.order_by('-updated_at')
    stock_summery = Item.objects.prefetch_related('item_name').values('item_name','quantity_at_hand').annotate(sum_stock_in = Sum(F('stock__stock_in'))).annotate(total_ordered_price = Sum('stock__total_cost_of_items')).annotate(sum_sold = F('sum_stock_in')-F('quantity_at_hand'))    
    
    item_cats = ItemCategory.get_all_item_categories()
    item_cat_id = request.GET.get('category')
    if item_cat_id != None:
        stocks = Stock.objects.order_by('-updated_at').filter(item__category = item_cat_id)
    context = {
        'stocks': stocks,
        'header': 'Manage Stocks',
        'item_cats':item_cats,
        'stock_summery':stock_summery
    }
    return render(request, 'stocks/stock_list.html', context)

@login_required
def save_all_stocks(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            stock =  Stock.objects.all()
            data['stock_list'] = render_to_string('includes/stocks/stock_list_2.html',{'stock': stock})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def stock_create(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)
    else:
        form = AddStockForm()
    return save_all_items(request, form, 'stocks/stock_create.html')

@login_required
def stock_delete(request, id):
    data = dict()
    stock = get_object_or_404(Stock, id=id)
    if request.method == "POST":
        item = Item.objects.get(id = stock.item.id)
        current_item_quantity = item.quantity_at_hand - stock.stock_in
        item.save()
        Item.objects.filter(id=item.id).update(quantity_at_hand = current_item_quantity)
        stock.delete()
        data['form_is_valid'] = True
        stocks = Stock.objects.all()
        data['stock_list'] = render_to_string('includes/stocks/stock_list_2.html', {'stocks': stocks})
    else:
        context = {'stock': stock}
        data['html_form'] = render_to_string('stocks/stock_delete.html', context, request=request)
    return JsonResponse(data)

