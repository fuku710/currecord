from django.urls import path
from django.views.generic import TemplateView
from .views import RecordList, RecordDetail, RecordCreate

urlpatterns = [
    path('', TemplateView.as_view(template_name='records/index.html')),
    path('records/', RecordList.as_view()),
    path('records/new/', RecordCreate.as_view()),
    path('records/<pk>/', RecordDetail.as_view()),
]
