from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surnames = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(max_length=100, null=True, blank=True)
    cel = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name} {self.surnames}" if self.surnames else self.name
    