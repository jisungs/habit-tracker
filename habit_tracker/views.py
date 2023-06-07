from django.http import HttpResponse
from django.shortcuts import render, redirect , get_object_or_404
from .models import Goal

# Create your views here.

def habits_list(request):
    return render(request, 'habit_tracker/habits_list.html' )

def habit_detail(request):
    goals = Goal.objects.filter(is_completed=False).order_by('-updated_at')
    
    completed_goals = Goal.objects.filter(is_completed=True)
    context = {
        'goals': goals,
        'completed_goals':completed_goals,
    }

    return render(request, 'habit_tracker/habit_detail.html', context)


def add_goal(request):
    goal = request.POST['goal']
    Goal.objects.create(goal=goal)
    return redirect('habit_detail')

def completed(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.is_completed = True
    goal.save()
    return redirect('habit_detail')

def undo_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.is_completed = False
    goal.save()
    return redirect('habit_detail')

def edit_goal(request, pk):
    return HttpResponse('Edit button is working')