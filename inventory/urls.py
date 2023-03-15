from django.urls import path
from django.contrib.auth import views as auth_views
from inventory.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('home/', home, name = 'home'),  
    path('inventory_dashboard/', inventory_dashboard, name = 'inventory_dashboard'),
    path('item_list/', item_list, name = 'items_list'),  
    path('item_create/', item_create, name = 'item_create'),
    path('item_update/<int:id>/', item_update, name = 'item_update'),
    path('item_delete/<int:id>/', item_delete, name = 'item_delete'),

    path('category_list/', category_list, name = 'category_list'),
    path('category_create/', category_create, name = 'category_create'),
    path('category_update/<int:id>/', category_update, name = 'category_update'),
    path('category_delete/<int:id>/', category_delete, name = 'category_delete'),

    path('unit_list/', unit_list, name = 'unit_list'),
    path('unit_create/', unit_create, name = 'unit_create'),
    path('unit_update/<int:id>/', unit_update, name = 'unit_update'),
    path('unit_delete/<int:id>/', unit_delete, name = 'unit_delete'),

    path('batch_list/', batch_list, name = 'batch_list'),
    path('batch_create/', batch_create, name = 'batch_create'),
    path('batch_update/<int:id>/', batch_update, name = 'batch_update'),
    path('batch_delete/<int:id>/', batch_delete, name = 'batch_delete'),

    path('stock_list/', stock_list, name = 'stock_list'),  
    path('stock_create/', stock_create, name = 'stock_create'),
    path('stock_delete/<int:id>/', stock_delete, name = 'stock_delete'),

    path('supplier_list/', supplier_list, name = 'supplier_list'),  
    path('supplier_create/', supplier_create, name = 'supplier_create'),
    path('supplier_update/<int:id>/', supplier_update, name = 'supplier_update'),
    path('supplier_delete/<int:id>/', supplier_delete, name = 'supplier_delete'),

]