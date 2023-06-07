from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list, name='habits_list'),
    path('habit_detail/', views.habit_detail, name='habit_detail'),

    path('habit_detail/addGoal/', views.add_goal, name ='add_goal')
]
