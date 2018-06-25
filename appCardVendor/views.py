from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vendor, Card
from django import forms

# Create your views here.

def index(request):
    return render(request, 'appCardVendor/index.html')

class VendorListView(ListView):
    model=Vendor

class VendorCreateView(CreateView):
    model = Vendor
    fields = ['name', 'url', 'username', 'password', 'card']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('vendor_list')
    def get_context_data(self, **kwargs):
        # get the default context data
        context = super(VendorCreateView, self).get_context_data(**kwargs)
        # add extra field to the context
        context['cards'] = Card.objects.all()
        return context
    
class VendorUpdateView(UpdateView):
    model = Vendor
    fields = ['name', 'url', 'username', 'password', 'card']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('vendor_list')
    def get_context_data(self, **kwargs):
        context = super(VendorUpdateView, self).get_context_data(**kwargs)
        context['cards'] = Card.objects.all()
        return context

class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendor_list')

class CardListView(ListView):
    model=Card

class CardCreateView(CreateView):
    model = Card
    fields = ['nickname', 'name_on_card', 'type', 'card_number', 'security_code', 'expiry_date']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('card_list')
        
class CardUpdateView(UpdateView):
    model = Card
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('card_list')

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('card_list')
        

    
