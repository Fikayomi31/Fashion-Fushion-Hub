# Generated by Django 5.1.5 on 2025-03-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_cart_qty_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
