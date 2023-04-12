from django.urls import path
from django.contrib.auth import views as auth_views
from sales.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('sales_list', sales_list, name = 'sales_list'),
    path('create_sales', create_sales, name = 'create_sales'),
]