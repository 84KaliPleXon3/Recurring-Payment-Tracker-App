from django.urls import path

from . import views

urlpatterns = [
    # home page 
    path('', views.index, name='index'),
    # Vendor Views
    path('vendors', views.VendorListView.as_view(), name='vendor_list'),
    path('vendor/create', views.VendorCreateView.as_view(), name='vendor_create_form'),
    path('vendor/<int:pk>/update', views.VendorUpdateView.as_view(), name='vendor_update_form'),
    path('vendor/<int:pk>/delete', views.VendorDeleteView.as_view(), name='vendor_confirm_delete'),
    # Card Views
    path('cards', views.CardListView.as_view(), name='card_list'),
    path('card/create', views.CardCreateView.as_view(), name='card_create_form'),
    path('card/<int:pk>/update', views.CardUpdateView.as_view(), name='card_update_form'),
    path('card/<int:pk>/delete', views.CardDeleteView.as_view(), name='card_confirm_delete'),
]

