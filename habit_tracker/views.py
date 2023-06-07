from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Goal

# Create your views here.

def habits_list(request):
    return render(request, 'habit_tracker/habits_list.html' )

def habit_detail(request):
    goals = Goal.objects.filter(is_completed=False).order_by('-updated_at')
    
    context = {
        'goals': goals,
    }

    return render(request, 'habit_tracker/habit_detail.html', context)


def add_goal(request):
    goal = request.POST['goal']
    Goal.objects.create(goal=goal)
    return redirect('habit_detail')