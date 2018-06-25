from django import forms
from .models import Vendor, Card

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'url', 'username', 'password', 'card')

    
        
        
                