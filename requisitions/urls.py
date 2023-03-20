from django.urls import path
from django.contrib.auth import views as auth_views
from inventory.views import *
from requisitions.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [  
    path('requisitions_list/', requisitions_list, name = 'requisitions_list'),  
    path('create_requisition/', create_requisition, name = 'create_requisition'), 
    path('item_details/<int:id>/', item_details, name = 'item_details'),
]