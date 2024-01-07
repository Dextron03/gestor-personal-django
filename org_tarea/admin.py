from django.contrib import admin
from . import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    pass 

admin.site.register(models.Task, TaskAdmin)