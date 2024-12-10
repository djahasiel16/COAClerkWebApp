from django.db import models
from django.utils import timezone

# Filing Inventory Entities:
# 1. Type
# 2. Filing Reference
# 3. Title
# 4. Remarks
# 5. Year
# 6. Fund
# Create your models here.

class Document(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    doc_year = models.IntegerField()
    doc_month = models.IntegerField()
    remarks = models.CharField(max_length=150)
    filing_ref = models.CharField(max_length=60)
    fund = models.CharField(max_length=10)
    date_received = models.DateField()
    time_received = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.FileField(upload_to="MultiFiles/Inventory/thumbnail", blank=True, null=True)
    attachment = models.FileField(upload_to="MultiFiles/Inventory/attachment", blank=True, null=True)
    status = models.CharField(max_length=20, default="unverified")
    office = models.CharField(max_length=100, default="ASDI")

    def __str__(self):
        return self.title