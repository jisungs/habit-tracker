from django.http import HttpResponse

from django.shortcuts import render, redirect , get_object_or_404
from .models import Goal, Task
from django.http import JsonResponse

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

def edit_goal(request, goal_id):
    get_goal = get_object_or_404(Goal, pk=goal_id)
    if request.method == 'POST':
        new_goal = request.POST['goal']
        get_goal.goal = new_goal
        get_goal.save()
        return redirect('habit_detail')
    else:
        context = {
            'get_goal': get_goal,
        }
        return render(request, 'habit_detail.html', context)

def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    return redirect('habit_detail')

def task(request):
    day_id = request.GET.get('day_id')

    todays_task = Task.objects.filter(day_id=day_id).values()

    parsed_data = list(todays_task)[0]
    date_id = parsed_data['day_id']
    subject = parsed_data['subject']
    content = parsed_data['desc']

    response_data = {
        "date_id": "DAY " + str(date_id),
        "title": str(subject),
        "content": str(content),
    }

    return JsonResponse(response_data)