from django.views.generic import ListView, DetailView, CreateView
from .models import Record
from .forms import RecordForm


class RecordList(ListView):
    model = Record
    context_object_name = 'records'


class RecordDetail(DetailView):
    model = Record


class RecordCreate(CreateView):
    model = Record
    form_class = RecordForm
