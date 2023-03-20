from dataclasses import field
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.views.generic import UpdateView
from django.db import models
from django_countries.fields import CountryField
# from constance.admin import ConstanceAdmin, ConstanceForm, Config
from djmoney.forms.widgets import MoneyWidget
from django.contrib.auth import authenticate, login, logout, get_user_model
from inventory.models import Item
from django.core.validators import RegexValidator

class CustomMoneyWidget(MoneyWidget):
    def format_output(self, rendered_widgets):
        return ('<div class="row form-group">'
                    '<div class="col-sm-12 ">%s</div>'
                    '<div class="col-sm-12 ">%s</div>'
                '</div>') % tuple(rendered_widgets)

class SearchForm(forms.ModelForm):
    barcode = forms.CharField(max_length=5, validators=[RegexValidator(r'^[0-9]', 'Only digit characters.')], widget = forms.TextInput(attrs={'autofocus': True, 'class': 'form-control pos_form','placeholder':'Enter Barcode','id':'barcode-input','type':'number'}) )   
    class Meta:
        model = Item
        fields = ('barcode',)