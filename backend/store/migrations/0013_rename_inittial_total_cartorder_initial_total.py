# Generated by Django 5.1.5 on 2025-03-07 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_tax_fee_cart_tax'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='inittial_total',
            new_name='initial_total',
        ),
    ]
