
from django.urls import path
from .views import diagnose


urlpatterns = [
    path("", diagnose, name="diagnose"),
]