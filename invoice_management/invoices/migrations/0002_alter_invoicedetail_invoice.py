# Generated by Django 4.2.16 on 2024-11-25 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='invoices.invoice'),
        ),
    ]
