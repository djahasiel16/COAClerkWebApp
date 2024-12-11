from django.db import models

# ASDI MODELS ----------------------------------------------------------------------------------
class ASDI_LFPS_DisbursmentVoucherRecord(models.Model):
    dte = models.DateField()
    no = models.IntegerField()
    check_no = models.IntegerField()
    asa_no = models.CharField(max_length=30)
    payee = models.CharField(max_length=255)
    nature_of_transaction = models.CharField(max_length=255)
    amountNetOfTax = models.DecimalField(decimal_places=3, max_digits=14)
    grossAmount = models.DecimalField(decimal_places=3, max_digits=14)

class ASDI_LFPS_AccountingEntriesRecord(models.Model):
    lfps_dv = models.ForeignKey(ASDI_LFPS_DisbursmentVoucherRecord, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)


class ASDI_COB_DisbursmentVoucherRecord(models.Model):
    dte = models.DateField()
    no = models.IntegerField()
    check_no = models.IntegerField()
    asa_no = models.CharField(max_length=30)
    payee = models.CharField(max_length=255)
    nature_of_transaction = models.CharField(max_length=255)
    amountNetOfTax = models.DecimalField(decimal_places=3, max_digits=14)
    grossAmount = models.DecimalField(decimal_places=3, max_digits=14)

class ASDI_COB_AccountingEntriesRecord(models.Model):
    lfps_dv = models.ForeignKey(ASDI_LFPS_DisbursmentVoucherRecord, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)


class ASDI_CARP_DisbursmentVoucherRecord(models.Model):
    dte = models.DateField()
    no = models.IntegerField()
    check_no = models.IntegerField()
    asa_no = models.CharField(max_length=30)
    payee = models.CharField(max_length=255)
    nature_of_transaction = models.CharField(max_length=255)
    amountNetOfTax = models.DecimalField(decimal_places=3, max_digits=14)
    grossAmount = models.DecimalField(decimal_places=3, max_digits=14)

class ASDI_CARP_AccountingEntriesRecord(models.Model):
    lfps_dv = models.ForeignKey(ASDI_LFPS_DisbursmentVoucherRecord, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)


# SDN MODELS -----------------------------------------------------------------------------------
class SDN_LFPS_DisbursmentVoucherRecord(models.Model):
    dte = models.DateField()
    no = models.IntegerField()
    check_no = models.IntegerField()
    asa_no = models.CharField(max_length=30)
    payee = models.CharField(max_length=255)
    nature_of_transaction = models.CharField(max_length=255)
    amountNetOfTax = models.DecimalField(decimal_places=3, max_digits=14)
    grossAmount = models.DecimalField(decimal_places=3, max_digits=14)

class SDN_LFPS_AccountingEntriesRecord(models.Model):
    lfps_dv = models.ForeignKey(SDN_LFPS_DisbursmentVoucherRecord, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)


class SDN_COB_DisbursmentVoucherRecord(models.Model):
    dte = models.DateField()
    no = models.IntegerField()
    check_no = models.IntegerField()
    asa_no = models.CharField(max_length=30)
    payee = models.CharField(max_length=255)
    nature_of_transaction = models.CharField(max_length=255)
    amountNetOfTax = models.DecimalField(decimal_places=3, max_digits=14)
    grossAmount = models.DecimalField(decimal_places=3, max_digits=14)

class SDN_COB_AccountingEntriesRecord(models.Model):
    lfps_dv = models.ForeignKey(SDN_LFPS_DisbursmentVoucherRecord, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)


class SDN_CARP_DisbursmentVoucherRecord(models.Model):
    dte = models.DateField()
    no = models.IntegerField()
    check_no = models.IntegerField()
    asa_no = models.CharField(max_length=30)
    payee = models.CharField(max_length=255)
    nature_of_transaction = models.CharField(max_length=255)
    amountNetOfTax = models.DecimalField(decimal_places=3, max_digits=14)
    grossAmount = models.DecimalField(decimal_places=3, max_digits=14)

class SDN_CARP_AccountingEntriesRecord(models.Model):
    lfps_dv = models.ForeignKey(SDN_LFPS_DisbursmentVoucherRecord, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)