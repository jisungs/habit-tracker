from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.html import strip_tags

from django.shortcuts import render, redirect , get_object_or_404
from .models import Goal, Task, WorkOut
from .forms import WorkOutForm
from accounts.models import Account
from django.contrib.auth.decorators import login_required



# Create your views here.
DAY_ID = 0

def set_day_id(request):
    global DAY_ID
    day_id = request.GET.get('day_id')
    DAY_ID = day_id
    print(DAY_ID)
    response_data = {
        "date_id": DAY_ID
    }
    return JsonResponse(response_data)
    

def habits_list(request):
    return render(request, 'habit_tracker/habits_list.html' )

@login_required(login_url='login')
def habit_detail(request):
    global DAY_ID
    current_user = request.user
    form = WorkOutForm(initial={'category': 'English'})

    goals = Goal.objects.filter(is_completed=False, user=current_user).order_by('-updated_at')
    workouts = WorkOut.objects.filter(user=current_user).order_by('-updated_at')
    completed_goals = Goal.objects.filter(is_completed=True)

    tasks = Task.objects.all().order_by('day_id')
    today_task = Task.objects.filter(is_completed = False).order_by('day_id').first()
    

    context = {
        'goals': goals,
        'completed_goals':completed_goals,
        'workouts':workouts,
        'tasks':tasks,
        'today_task':today_task,
        'day_id':DAY_ID,
        'form':form

    }

    return render(request, 'habit_tracker/habit_detail.html', context)


def add_goal(request):
    current_user = request.user
    goal = request.POST['goal']
    Goal.objects.create(goal=goal, user= current_user)
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

@login_required(login_url='login')
#Create workout content
def create_work_out(request):
    global DAY_ID
    today_task = Task.objects.filter(is_completed = False).order_by('day_id').first()
    if DAY_ID == 0:  
        day_id = today_task.day_id
    else: 
        day_id = DAY_ID

    if request.method == "POST":
        form = WorkOutForm(request.POST)
        form.initial['category'] = 'English'
        # print(form.errors)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            
            # Get a valid Task instance (replace 1 with the appropriate task ID)

            workout = form.save(commit=False)
            workout.user = user
            workout.category = category
            workout.title = title
            workout.content = content
            
            day_id = day_id  # Replace with the ID of the desired Task instance
            task =  Task.objects.filter(day_id=day_id).first()
            task.is_completed = True
            workout.task = task
            workout.category = category
            workout.save()
            task.save()
            DAY_ID=0
            return redirect('habit_detail')
    else:
        form = WorkOutForm()

    context = {
            'form':form,
    }

    return render(request, 'habit_tracker/habit_detail.html', context)

def get_workout(request):
    if request.method == "GET":
        day_id = request.GET.get('day_id')
        try:
            task  = Task.objects.get(day_id=day_id)
            workout = task.workout_set.first()

            if workout: 
                response_data = {
                    'date_id':day_id,
                    'title':workout.title,
                    'content':workout.content,
                    'updated_date':workout.updated_at,
                }
            else:
                response_data = {
                    'date_id': day_id,
                    'title': "No Workout Available",
                    'content': "Start your workout routine!",
                }

            return JsonResponse(response_data)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)