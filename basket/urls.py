from django.urls import path

from  basket.views import basket_add, basket_remove
app_name = 'basket'

urlpatterns = [
    # path('', basket_detail, name='basket_detail'),
    path('add/<int:item_id>/', basket_add, name='basket_add'),
    path('remove/<int:item_id>/', basket_remove, name='basket_remove'),

]
