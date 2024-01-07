from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, null= False, blank=False)
    description = models.TextField(max_length=1500, null=True, blank=True)
    hour_completion = models.TimeField(auto_now=False, auto_now_add=False, editable=True, blank=True, null= True)
    date_completion = models.DateField(auto_now=False, auto_now_add=False, editable=True, blank=True, null= True)
    
    def __str__(self) -> str:
        return self.title    