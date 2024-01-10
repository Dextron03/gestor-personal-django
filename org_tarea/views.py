from django.shortcuts import render, redirect
from . import form
from . import models
from django.contrib import messages

# Create your views here.
def index(request):
    tasks = models.Task.objects.filter(title__contains=request.GET.get('search', ""))
    tasks_sorted = sorted(tasks, key=lambda x: x.priority, reverse=True)
    return render(request, "org_tarea/index_task.html", {"tasks":tasks_sorted})

def add_task(request):
    
    if request.method == "GET":
        form_task = form.TaskForm()
        return render(request, "org_tarea/new_task.html", {"form":form_task})
    
    if  request.method == "POST":
        form_task = form.TaskForm(request.POST)
        if form_task.is_valid():
            form_task.save()
            return redirect('home_tasks')
        return render(request, "org_tarea/new_task.html", {"form":form_task})
        
def detele_task(request, id):
    task = models.Task.objects.get(id = id) 
    if request.method == "GET":
        task.delete()
        messages.success(request, "La tarea asido eliminada")
        return redirect("home_tasks")
    return render(request, "org_tarea/index_task.html", {"tasks":task})

def edit_task(request, id):
    task_edit = models.Task.objects.get(id=id)
    if request.method == "GET":
        form_edit = form.TaskForm(instance=task_edit)
        return render(request, "org_tarea/edit_task.html", {"form":form_edit, "id":id})
    
    if request.method == "POST":
        form_edit = form.TaskForm(request.POST, instance=task_edit)
        if form_edit.is_valid():
            form_edit.save()
            messages.success(request, "La tarea a sido actulizada correctamente.")
            return redirect("home_tasks")
        return render(request, "org_tarea/edit_task.html", {"form":form_edit, "id":id})
