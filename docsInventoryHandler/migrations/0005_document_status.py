# Generated by Django 5.0.6 on 2024-10-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsInventoryHandler', '0004_document_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(default='unverified', max_length=20),
        ),
    ]
