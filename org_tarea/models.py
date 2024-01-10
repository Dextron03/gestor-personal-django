from django.db import models
from django.core import validators

class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1500, null=True, blank=True)
    priority = models.PositiveSmallIntegerField(default=1, help_text='A mayor número, mayor prioridad.(El maximo es 3.)')
    hour_completion = models.TimeField(null=True, blank=True)
    date_completion = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
