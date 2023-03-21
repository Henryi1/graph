from django.shortcuts import render
from .models import Task

def index(request):
    if request.method == 'POST':
        if request.POST.get('task'):
            task = Task()
            task.title = request.POST.get('task')
            task.save()
    else:
        tasks = Task.objects.all()
        return render(request, 'tasks/list.html', {'tasks': tasks})
