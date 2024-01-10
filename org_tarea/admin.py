from django.contrib import admin
from . import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "priority")
    list_filter = ['title','priority', 'date_completion']

admin.site.register(models.Task, TaskAdmin) 
