from django import forms
from datetime import date
from django.forms import widgets
from django.forms import SelectDateWidget

from .models import Vendor, Card

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

        
class CardForm(forms.ModelForm):
    security_code = forms.CharField(
        min_length=3,
        max_length=4,
    )
    expiry_date = forms.DateField(
        widget=SelectDateWidget(),
    )
    class Meta:    
        model = Card
        fields = ['nickname', 'name_on_card', 'type', 'card_number', 'security_code', 'expiry_date']