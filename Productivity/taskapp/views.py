from django.shortcuts import render
from taskapp.models import TaskList



# Create your views here.

def taskHome(request):
    all_tasks = TaskList.objects.all

    context = {
        "tasks":all_tasks,
        
    }
    return render(request, "task.html",context)