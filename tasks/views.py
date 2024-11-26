from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse
from django.urls import reverse


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        Task.objects.create(title=title, description=description, deadline=deadline)
        return redirect(reverse('task_list'))

    return render(request, 'tasks/task_form.html')


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.status = 'status' in request.POST
        task.save()
        return redirect(reverse('task_list'))

    return render(request, 'tasks/task_form.html', {'task': task})



def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('task_list'))

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

