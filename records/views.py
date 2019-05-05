from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from django.urls import reverse_lazy
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


class RecordUpdate(UpdateView):
    model = Record
    form_class = RecordForm


class RecordDelete(DeleteView):
    model = Record
    success_url = reverse_lazy('records-list')
