from django.contrib import admin
from inventory.models import Unit, ItemCategory, Item, BatchNumber, Stock, Supplier

admin.site.register(Unit)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(BatchNumber)
