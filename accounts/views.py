from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Count
from django.utils import timezone
from datetime import datetime
from django.contrib import messages


@login_required
def logout_request(request):
    logout(request)
    response = redirect('logout')
    response.delete_cookie('modalShown')
    return response


