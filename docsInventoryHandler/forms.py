from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    FUND_CHOICES = [
        ('LFPS', '501 LFPS'),
        ('COB', '501 COB'),
        ('CARP', '501 CARP'),
    ]

    MONTH_CHOICES = [
        (1,'January'),
        (2,'February'),
        (3,'March'),
        (4,'April'),
        (5,'May'),
        (6,'June'),
        (7,'July'),
        (8,'August'),
        (9,'September'),
        (10,'October'),
        (11,'November'),
        (12,'December'),
    ]

    OFFICE_CHOICES = [
        ('ASDI','ASDI'),
        ('SDN','SDN'),
    ]

    STATUS_CHOICES = [
        ('verified','Verified'),
        ('unverified','Unverified')
    ]

    DOCUMENT_TITLE = [
        ('Bank Reconciliation Statement','Bank Reconciliation Statement'),
        ('Liquidation Report', 'Liquidation Report'),
        ('Report of Check Issued', 'Report of Check Issued'),
        ('Report of Disbursement', 'Report of Disbursement'),
        ('Report of Debit Account','Report of Debit Account'),
        ('Report of Accountability for Accountable Form', 'Report of Accountability for Accountable Form'),
        ('Monthly Equipment Report', 'Monthly Equipment Report')
    ]

    fund = forms.ChoiceField(choices=FUND_CHOICES, label='Related Fund')
    doc_month = forms.ChoiceField(choices=MONTH_CHOICES, label='Month of Document')
    office = forms.ChoiceField(choices=OFFICE_CHOICES, label='Satellite Office')
    status = forms. ChoiceField(choices=STATUS_CHOICES, label='Status')
    title = forms.ChoiceField(choices=DOCUMENT_TITLE, label='Document Title', widget=forms.Select)

    class Meta:
        model = Document
        fields = [
            'type',
            'office',
            'title',
            'description',
            'doc_year',
            'doc_month',
            'date_received',
            'time_received',
            'remarks',
            'filing_ref',
            'fund',
            'attachment',
            'thumbnail',
            'status'
        ]

        labels = {
            'type':'Document Type',
            'office':'Satellite Office',
            'title':'Document Title',
            'description':'Brief Description',
            'date_received':'Date Received',
            'time_received':'Time Received',
            'doc_year':'Year of Document',
            'doc_month':'Month of Document',
            'remarks':'Additional Remarks',
            'filing_ref':'Filing Reference',
            'fund':'Related Fund',
            'status':'Status'
        }

        widgets = {
            'type':forms.TextInput(attrs={'class':'form-control'}),
            'office':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.Select(attrs={'class':'form-check-input'}),
            'description': forms.Textarea(attrs={'rows':4, 'cols':15}),
            'date_received': forms.DateInput(attrs={'type':'date'}),
            'time_received': forms.TimeInput(attrs={'type':'time'}),
            'attachment': forms.FileInput(attrs={'class':'form-control', 'type':'file'}),
            'thumbnail': forms.FileInput(attrs={'class':'form-control', 'type':'file'}),
        }

class FilterForm(forms.Form):
    start_date = forms.DateField(input_formats="Y-m-d")
    end_date = forms.DateField(input_formats="Y-m-d")
    fund = forms.CharField(max_length=10)