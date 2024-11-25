from django.db import models

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=30)
    date = models.DateTimeField()

class InvoiceDetail(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def line_total(self):
        return (self.unit_price * self.quantity)