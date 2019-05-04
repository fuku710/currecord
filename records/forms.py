from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'date', 'note']
        widgets = {
            'date': forms.SelectDateWidget()
        }
