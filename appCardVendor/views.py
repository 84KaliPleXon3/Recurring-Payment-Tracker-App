from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vendor, Card
from .forms import VendorForm, CardForm

# Create your views here.

def index(request):
    return render(request, 'appCardVendor/index.html')

class VendorListView(ListView):
    model=Vendor

class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    
    
class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    def get_context_data(self, **kwargs):
        context = super(VendorUpdateView, self).get_context_data(**kwargs)
        # get the card object corresponding to the vendor 
        context['card'] = self.object.card 
        return context

def load_card_data(request):
    card_id = request.GET.get('card')
    card = Card.objects.get(pk=card_id)
    return render(request, 'appCardVendor/load_card_data.html', {'card': card})
    
class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendor_list')

class CardListView(ListView):
    model=Card

class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('card_list')
        
class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('card_list')

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('card_list')
        

    
