from django.urls import path
from django.contrib.auth import views as auth_views
from reports.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [  
    path('fast_selling_product/', fast_selling_product, name = 'fast_selling_product'),  
]