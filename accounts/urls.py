from django.urls import path
from . import views

urlpatterns = [
     path('policy/' , views.policy, name='policy'),
     path('register/', views.register, name='register'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),

     path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]