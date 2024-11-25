from django.urls import path
from .views import InvoiceCreateView
from .views import InvoiceListView

urlpatterns = [
    # path("", InvoiceCreateView.as_view(), name='invoice-create')
    path("", InvoiceListView.as_view(), name='invoice-list')
]