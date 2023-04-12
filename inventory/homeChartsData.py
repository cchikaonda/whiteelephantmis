from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render,redirect, get_object_or_404
from inventory.models import ItemCategory, Unit, Item, Stock, Supplier
from inventory.forms import *
from django.template.loader import render_to_string

from constance import config
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.db.models import AutoField,IntegerField,FloatField,ExpressionWrapper, F, DecimalField, Count, Sum
from djmoney.money import Money
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.db.models.functions import Lower
from djmoney.models.fields import MoneyField
from accounts.forms import *
from requisitions.models import RequestItem, Requisition

def get_requests_this_week():
    week_start = date.today()
    week_start -= timedelta(days=week_start.weekday())
    week_end = week_start + timedelta(days=6)
    requests_this_week = RequestItem.objects.filter(created_at__gte=week_start, created_at__lt=week_end)
    return requests_this_week
    
def get_requests_last_week():
    some_day_last_week = date.today() - timedelta(days=7)
    monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    monday_of_this_week = monday_of_last_week + timedelta(days=7)
    requests_lastweek = RequestItem.objects.filter(created_at__gte=monday_of_last_week, created_at__lt=monday_of_this_week)
    return requests_lastweek