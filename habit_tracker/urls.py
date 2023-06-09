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
    path('habit_detail/edit_goal/<int:goal_id>/', views.edit_goal, name ='edit_goal'),
    # Delete goal
    path('delete_goal/<int:pk>', views.delete_goal, name='delete_goal' ),
    #Today's Task contents 
    path('today_task/', views.task, name='task'),

]
