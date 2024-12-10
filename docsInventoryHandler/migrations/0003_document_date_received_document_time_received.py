# Generated by Django 5.0.6 on 2024-10-17 06:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsInventoryHandler', '0002_document_created_at_document_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='date_received',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='document',
            name='time_received',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]