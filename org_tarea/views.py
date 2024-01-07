from django.shortcuts import render
from . import form
# Create your views here.

def org_task(request):
    
    if request.method == "GET":
        form_task = form.TaskForm(request.GET)
        return render(request, "org_tarea/to_do_form.html", {"form":form_task})
    
    if  request.method == "POST":
        form_task = form.TaskForm(request.POST)
        if form_task.is_valid():
            form_task.save()
            return render(request, "org_tarea/to_do_form.html", {"form":form_task})
        else:
            return render(request, "error.html", {})
