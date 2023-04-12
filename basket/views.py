from django.shortcuts import render, redirect, get_object_or_404
from .basket import Basket
from inventory.models import Item
from .forms import BasketAddProductForm
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from djmoney.money import Money
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib import messages
# @require_POST
def basket_add(request, item_id):
    basket = Basket(request)
    item = get_object_or_404(Item, id = item_id)
    if request.method == "POST":
        qty = int(request.POST.get('qty'))
        if item.quantity_at_hand < int(qty):
            itemqty = str(item.quantity_at_hand )
            item_name = str(item.item_name )
            item_unit = str(item.unit)
            messages.error(request, "There are only " + itemqty  + " "+ item_unit + "(s) of " + item_name + " in Inventory")
        else:
            basket.add(item = item, qty = qty, override_qty='override')
    return redirect ('create_requisition')

def basket_remove(request, item_id):
    basket = Basket(request)
    item = get_object_or_404(Item, id = item_id)
    basket.delete(item.id)
    return redirect ('create_requisition')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket':basket})


