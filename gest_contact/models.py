from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surnames = models.CharField(max_length=100, null=True, blank=True)
    cel = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.name} {self.surnames}" if self.surnames else self.name
    