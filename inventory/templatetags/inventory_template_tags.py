from django import template
from inventory.models import *


register = template.Library()

@register.filter
def user_count(user):
    if user.is_authenticated:
        qs = User.objects.all().count()
    return qs

@register.filter
def item_category_count(user):
    if user.is_authenticated:
        qs = ItemCategory.objects.all().count()
    return qs

@register.filter
def item_count(user):
    if user.is_authenticated:
        qs = Item.objects.all().count()
    return qs

@register.filter
def unit_count(user):
    if user.is_authenticated:
        qs = Unit.objects.all().count()
    return qs

@register.filter
def supplier_count(user):
    if user.is_authenticated:
        qs = Supplier.objects.all().count()
    return qs

@register.filter
def stock_count(user):
    if user.is_authenticated:
        qs = Stock.objects.all().count()
    return qs

@register.filter
def batch_number_count(user):
    if user.is_authenticated:
        qs = BatchNumber.objects.all().count()



