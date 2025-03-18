# Generated by Django 5.1.5 on 2025-03-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cartorderitem_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='coupon_code',
            new_name='code',
        ),
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
