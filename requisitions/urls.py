from django.urls import path
from django.contrib.auth import views as auth_views
from inventory.views import *
from requisitions.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [  
    path('requisitions_list/', requisitions_list, name = 'requisitions_list'),  
    path('create_requisition/', create_requisition, name = 'create_requisition'),
    path('edit_requisition/<int:id>/', edit_requisition, name = 'edit_requisition'), 
    path('item_details/<int:id>/', item_details, name = 'item_details'),
    path('submit_requisition/', submit_requisition, name = 'submit_requisition'),
    path('approve_requisition/<int:id>/', approve_requisition, name = 'approve_requisition'),

    path('remove_single_item_from_cart/<slug>/', remove_single_item_from_cart, name = 'remove_single_item_from_cart'),
    path('add_single_item_from_cart/<slug>/', add_single_item_from_cart, name = 'add_single_item_from_cart'),
    
    
]