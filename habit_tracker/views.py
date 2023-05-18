from django.shortcuts import render

# Create your views here.

def habits_list(request):
    return render(request, 'habit_tracker/habits_list.html' )