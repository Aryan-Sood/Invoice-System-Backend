from django.urls import path
from .views import InvoiceCreateView,InvoiceListView, InvoiceDetailView, DeleteAllInvoices, DeleteInvoiceById

urlpatterns = [
    path("", InvoiceListView.as_view(), name='invoice-list'),
    path("/create", InvoiceCreateView.as_view(), name='invoice-create'),
    path("/detail", InvoiceDetailView.as_view(), name='invoice-detail'),
    path("/deleteall", DeleteAllInvoices.as_view(), name='delete-all'),
    path('/deletebyid', DeleteInvoiceById.as_view(), name='delete-by-id')
]