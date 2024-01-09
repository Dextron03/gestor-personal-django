from django.db import models
from django.core import validators
from django.utils.html import format_html


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surnames = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(max_length=100, null=True, blank=True)
    cel = models.CharField(max_length=12, null=False, blank=False, validators=[validators.MaxLengthValidator(limit_value=12, message=format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Tu numero de telefono no es valido. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))])
    email = models.EmailField(validators=[validators.EmailValidator(message=format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Ingresa una dirección de correo electrónico válida <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))])
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name} {self.surnames}" if self.surnames else self.name
    