from django import forms
from django.core.exceptions import ValidationError
from django.db.models import F
from inventory.models import Item


from django.core.exceptions import ValidationError
from django.db.models import F

def validate_basket_item_quantity(value, product_id):
    max_quantity = Item.objects.values_list(F('quantity_at_hand'), flat=True).get(id=product_id)
    if value > max_quantity:
        raise ValidationError('The entered quantity is greater than the available quantity.')


class BasketAddProductForm(forms.Form):
    quantity = forms.IntegerField(validators=[validate_basket_item_quantity])
    override = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)

    