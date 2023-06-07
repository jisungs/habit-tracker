from django.urls import path
from . import views

urlpatterns = [
    path('', views.habits_list, name='habits_list'),

    path('habit_detail/', views.habit_detail, name='habit_detail'),
    # add goals 
    path('habit_detail/addGoal/', views.add_goal, name ='add_goal'),
    #completed the goals 
    path('habit_detail/completed/<int:pk>', views.completed, name ='completed'),
    # undo the goals 
    path('habit_detail/undo_goal/<int:pk>', views.undo_goal, name ='undo_goal'),
    # Edit goal
    path('habit_detail/edit_goal/<int:pk>', views.edit_goal, name ='edit_goal'),

]
