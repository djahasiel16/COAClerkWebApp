from django.contrib import admin
from .models import ASDI_LFPS_DisbursmentVoucherRecord, ASDI_LFPS_AccountingEntriesRecord

# Register your models here.
admin.site.register(ASDI_LFPS_DisbursmentVoucherRecord)
admin.site.register(ASDI_LFPS_AccountingEntriesRecord)