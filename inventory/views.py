from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
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



# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def inventory_dashboard(request):
    pass

@login_required
def item_list(request):
    pass

@login_required
def save_all_items(request, form, template_name):
    pass

@login_required
def item_create(request):
    pass

@login_required
def item_update(request, id):
    pass

@login_required
def item_delete(request, id):
    pass


@login_required
def supplier_list(request):
    pass

@login_required
def save_all_suppliers(request, form, template_name):
    pass

@login_required
def supplier_create(request):
    pass

@login_required
def supplier_update(request, id):
    pass

@login_required
def supplier_delete(request, id):
    pass

@login_required
def category_list(request):
    pass

@login_required
def save_all_categories(request, form, template_name):
    pass
@login_required
def category_create(request):
    pass

@login_required
def category_update(request, id):
    pass

@login_required
def category_delete(request, id):
    pass

@login_required
def unit_list(request):
    pass

@login_required
def save_unit_list(request, form, template_name):
    pass

@login_required
def unit_create(request):
    pass

@login_required
def unit_update(request, id):
    pass

@login_required
def unit_delete(request, id):
    pass

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
    pass

@login_required
def save_all_batches(request, form, template_name):
    pass

@login_required
def batch_create(request):
    pass

@login_required
def batch_update(request, id):
    pass

@login_required
def batch_delete(request, id):
    pass

def view_batch_details(request, batch_id):
    pass


@login_required
def stock_list(request):
    pass

@login_required
def save_all_stocks(request, form, template_name):
    pass

@login_required
def stock_create(request):
    pass

@login_required
def stock_delete(request, id):
    pass
