from django.contrib import admin
from sales.models import ShelfItem, SoldItem, Sale

admin.site.register(ShelfItem)
admin.site.register(SoldItem)
admin.site.register(Sale)
