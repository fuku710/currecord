from django.views.generic import CreateView
from .models import Record
from .forms import RecordForm


class RecordCreate(CreateView):
    model = Record
    form_class = RecordForm
