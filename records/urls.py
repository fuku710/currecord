from django.urls import path
from django.views.generic import TemplateView
from .views import RecordList, RecordDetail, RecordCreate, RecordUpdate, RecordDelete

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='records/index.html'), name='records-top'),
    path('records/', RecordList.as_view(), name='records-list'),
    path('records/new/', RecordCreate.as_view(), name='records-new'),
    path('records/<pk>/', RecordDetail.as_view(), name='records-detail'),
    path('records/<pk>/edit/', RecordUpdate.as_view(), name='records-edit'),
    path('records/<pk>/delete/', RecordDelete.as_view(), name='records-delete'),
]
