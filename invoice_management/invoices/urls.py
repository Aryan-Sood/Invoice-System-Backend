from django.urls import path
from .views import InvoiceCreateView

urlpatterns = [
    path("", InvoiceCreateView.as_view(), name='invoice-create')
]