from django.db import models
from django.core import validators
from django.utils.html import format_html


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surnames = models.CharField(max_length=100, blank=True)
    note = models.TextField(max_length=100, null=True, blank=True)
    cel = models.CharField(max_length=12, null=False, blank=False, help_text='Escribir el número sin guiones (-).', validators=[validators.MaxLengthValidator(limit_value=10, message=format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Tu número de teléfono no es válido. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))])
    email = models.EmailField(validators=[validators.EmailValidator(message=format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Ingresa una dirección de correo electrónico válida <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))])
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    img_contact = models.ImageField(upload_to="profile/", default="profile/profile.png", blank=True, null=True, validators=[validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'], message=format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Solo acepta archivos png y jpg <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))])
    
    def __str__(self) -> str:
        return f"{self.name} {self.surnames}" if self.surnames else self.name
