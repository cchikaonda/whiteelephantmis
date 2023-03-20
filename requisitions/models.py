from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User
from django.shortcuts import reverse

from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, pre_save
from inventory.models import *
from django.dispatch import receiver
from datetime import date, timedelta, datetime, time

# Create your models here.

class RequestItem(models.Model):
    request_id = models.CharField(default="", max_length=30)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    requested = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    requested_item_price = MoneyField(max_digits=14, decimal_places=2, default_currency='MWK', default= 0.0)
    requested_items_total = MoneyField(max_digits=14, decimal_places=2, default_currency='MWK', default= 0.0)
    requested_time = models.DateTimeField(auto_now_add=True, null = True)

request_status = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivered', 'Delivered'),
    )
    
class Requisition(models.Model):
    def gen_code(self):
            return 'RQT%04d'%self.pk
    code = models.CharField(max_length=50, null=True, default="0000")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(RequestItem)
    requested = models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=request_status, default="Pending")
    request_total_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='MWK', default= 0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_code(self):
        return self.gen_code
