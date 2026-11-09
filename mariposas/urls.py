from django.urls import path
from . import views

app_name = 'mariposas'

urlpatterns = [
  path('', views.inicio, name='inicio'),
]