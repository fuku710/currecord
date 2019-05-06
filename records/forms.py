from django import forms
from django.utils import timezone
from .models import Record

year = timezone.now().year

YEARS = list(range(year - 5, year + 1))


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'date', 'note', 'image']
        widgets = {
            'date': forms.SelectDateWidget(years=YEARS)
        }
