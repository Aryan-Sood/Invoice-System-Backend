# Generated by Django 4.2.16 on 2024-11-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_invoicedetail_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='line_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
