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
from django.contrib.auth.models import Group, Permission, User
from .forms import *

from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

@login_required
def logout_request(request):
    logout(request)
    response = redirect('logout')
    response.delete_cookie('modalShown')
    return response

def user_list(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'users/user_list.html', context)

@login_required
def save_all_users(request,form,template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			users = User.objects.exclude(email = request.user)
			data['user_list'] = render_to_string('includes/users/user_list_2.html',{'users':users})
		else:
			data['form_is_valid'] = False
	context = {
	'form':form
	}
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)


@login_required
def user_create(request):
	
	if request.method == 'POST':
		form = UserAdminCreationForm(request.POST)
	else:
		form = UserAdminCreationForm()
	return save_all_users(request,form,'users/user_create.html')


@login_required
def user_update(request,id):
	user = get_object_or_404(User,id=id)
	if request.method == 'POST':
		form = EditUserPermissionsForm(request.POST,instance=user)
	else:
		form = EditUserPermissionsForm(instance=user)
	return save_all_users(request,form,'users/user_update.html')

@login_required
def user_delete(request,id):
	data = dict()
	user = get_object_or_404(User,id=id)
	if request.method == "POST":
		user.delete()
		data['form_is_valid'] = True
		users = User.objects.exclude(email = request.user)
		data['user_list'] = render_to_string('users/user_list_2.html',{'users':users})
	else:
		context = {'user':user}
		data['html_form'] = render_to_string('users/user_delete.html',context,request=request)
	return JsonResponse(data)

