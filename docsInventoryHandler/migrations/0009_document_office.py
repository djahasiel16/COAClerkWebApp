# Generated by Django 5.0.6 on 2024-10-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsInventoryHandler', '0008_alter_document_doc_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='office',
            field=models.CharField(default='ASDI', max_length=100),
        ),
    ]