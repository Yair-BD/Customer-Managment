from django.db.models import fields
from .views import *
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta :
        model = Order
        fields = "__all__"
