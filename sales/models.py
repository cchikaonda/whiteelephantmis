from django.db import models
from inventory.models import Item
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class ShelfItem(models.Model):
    shelf_item = models.ForeignKey(Item, on_delete = models.CASCADE)
    current_quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.shelf_item.item_name


class SoldItem(models.Model):
    item = models.ForeignKey(ShelfItem, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    sold = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    sold_price = MoneyField(max_digits=14, decimal_places=2, default_currency='MWK', default= 0.0)
    def __str__(self):
        return f"{self.quantity} {self.item.shelf_item.unit} of {self.item.shelf_item}"


class Sale(models.Model):
    def gen_code(self):
            return 'ORD%04d'%self.pk
    code = models.CharField(max_length=50, null=True, default="0000")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(SoldItem)
    sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
