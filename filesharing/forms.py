from django import forms
from .models import MultiDocument

class MultiDocumentForm(forms.ModelForm):
    class Meta:
        model = MultiDocument
        fields = ['title', 'file']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'file':forms.FileInput(attrs={'class':'form-control'})
        }