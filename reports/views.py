from django.shortcuts import render
from inventory.models import Item, ItemCategory
from requisitions.models import Requisition, RequestItem
from djmoney.money import Money

# Create your views here.

def fast_selling_product(request):
    items = Item.get_all_items() 
    ordered_items = RequestItem.objects.all()
    fastselling = []
    for item in items:
        dict = {}
        dict['item']=item.item_name
        dict['category']=item.category
        dict['total']= get_total_requested(item)
        dict['price'] = get_sold_price(item)
        dict['amount'] = get_total_requested(item) * get_sold_price(item)
        fastselling.append(dict)

        # sort selling items in descending order
        fastselling = sorted(fastselling, key=lambda x:x['total'], reverse=True)
    context = {
        "header": 'Selling Product Report' ,
        "items":items,
        "ordered_items":ordered_items,
        "fastselling":fastselling,
    }
    return render(request, 'fast_selling_product.html', context)

def get_total_requested(item):
    total_requested = 0
    requested_items = RequestItem.objects.filter(item = item)
    for requested_item in requested_items:
        total_requested += requested_item.quantity
    return total_requested

def get_sold_price(item):
    requested_item = RequestItem.objects.filter(item=item).last()
    if requested_item:
        requested_item_price = requested_item.requested_item_price
        return requested_item_price
    else:
        return item.price

def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.total(), key = lambda x: x[1], reverse = reverse))

    
