# Generated by Django 5.1.5 on 2025-03-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_inittial_total_cartorder_initial_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='initial_total',
            new_name='initial_cost',
        ),
    ]
