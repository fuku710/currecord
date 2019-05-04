from django.urls import path
from .views import RecordCreate

urlpatterns = [
    path('', RecordCreate.as_view())
]
