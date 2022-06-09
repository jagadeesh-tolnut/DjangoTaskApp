from django.shortcuts import render

# Create your views here.

def taskHome(request):
    context = {
        "content":"Hello Vishwa, How are you?",
    }
    return render(request, "task.html",context)