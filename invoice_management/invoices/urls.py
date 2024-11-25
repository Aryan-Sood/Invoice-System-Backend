from django.urls import path
from .views import InvoiceCreateView,InvoiceListView, InvoiceDetailView

urlpatterns = [
    # path("", InvoiceCreateView.as_view(), name='invoice-create')
    path("", InvoiceListView.as_view(), name='invoice-list'),
    path("/detail", InvoiceDetailView.as_view(), name='invoice-detail')
]