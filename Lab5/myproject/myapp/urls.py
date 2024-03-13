# myapp/urls.py
from django.urls import path
from .views import add_view, display_view

urlpatterns = [
    path('add/', add_view, name='add'),
    path('display/', display_view, name='display'),
]
