from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LoginView.as_view(), name = 'logout'),
    path('logout_request', logout_request, name = 'logout_request'),
    path('user_list', user_list, name = 'user_list'),
    path('user_create', user_create, name = 'user_create'),
    path('user_update/<int:id>/', user_update, name = 'user_update'),
    path('user_delete/<int:id>/', user_delete, name = 'user_delete'),
]