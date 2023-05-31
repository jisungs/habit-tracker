from django.shortcuts import render

# Create your views here.

def habits_list(request):
    return render(request, 'habit_tracker/habits_list.html' )

def habit_detail(request):
    return render(request, 'habit_tracker/habit_detail.html')