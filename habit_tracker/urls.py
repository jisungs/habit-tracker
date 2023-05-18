from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list, name='habits_list'),
]
