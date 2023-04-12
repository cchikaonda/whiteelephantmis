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
from djmoney.money import Money
from common_utils.BaseModels import BaseModel
# Create your models here.

class RequestItem(BaseModel):
    request_id = models.CharField(default="", max_length=30)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    approved = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    approved_qty = models.IntegerField(default=0)
    requested_item_price = MoneyField(max_digits=14, decimal_places=2, default_currency='MWK', default= 0.0)
    requested_time = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return f"{self.quantity} {self.item.unit} of {self.item.item_name}"
    
    def total_approved_item_amount(self):
        amount = MoneyField()
        amount = self.approved_qty * self.requested_item_price
        return amount

    def get_item_balance(self):
        balance = self.item.quantity_at_hand - self.approved_qty
        return balance

    @property
    def amount(self):
        amount = Money(0.0, 'MWK')
        amount = self.quantity * self.requested_item_price
        return amount

request_status = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Not Approved', 'Not Approved'),
    )
    
class Requisition(BaseModel):
    def gen_code(self):
            return 'RQT%04d'%self.pk
    code = models.CharField(max_length=50, null=True, default="0000")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(RequestItem)
    status = models.CharField(max_length=15, choices=request_status, default="Pending")
    request_total_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='MWK', default= 0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Manager')
    class Meta:
         ordering = ['code']
         permissions = [("can_approve_requisition", "can approve requisition"), ("can_view_all_requisitions", "can view all requsitions")]

    @property
    def get_code(self):
        return self.gen_code
    
    def get_total_approved_request_amount(self):
        total = Money(0.0, 'MWK')
        for item in self.items.all():
            total += item.total_approved_item_amount()
        return total
    
    def __str__(self):
        return '{1} {0}'.format(self.created_at, self.user)

            
