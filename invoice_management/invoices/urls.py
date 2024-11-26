from django.urls import path
from .views import InvoiceCreateView,InvoiceListView, InvoiceDetailView, DeleteAllInvoices

urlpatterns = [
    path("/create", InvoiceCreateView.as_view(), name='invoice-create'),
    path("", InvoiceListView.as_view(), name='invoice-list'),
    path("/detail", InvoiceDetailView.as_view(), name='invoice-detail'),
    path("/deleteall", DeleteAllInvoices.as_view(), name='delete-all')
]