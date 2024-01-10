from django import forms
from . import models
from django.utils.html import format_html

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mt-2", 'placeholder': "Nombre del contacto"}),
            "surnames": forms.TextInput(attrs={"class": "form-control mt-2", 'placeholder': "Apellido del contacto"}),
            "note": forms.Textarea(attrs={"class": "form-control mt-2", 'placeholder': "¿Quieres agregar un recordatorio?"}),
            "cel": forms.NumberInput(attrs={"class": "form-control mt-2", 'placeholder': "Número de teléfono"}),
            "email": forms.EmailInput(attrs={"class": "form-control mt-2", 'placeholder': "ejemplo@gmail.com"}),
            "img_contact": forms.FileInput(attrs={"class": "form-control mt-2", "type": "file"}),
        }
        
        labels = {
            "name": "Nombres",
            "surnames": "Apellidos",
            "note": "Nota",
            "cel": "Número",
            "img_contact": "Foto de Perfil"
        }
        
        error_messages = {
            'name': {'required': ""},
            'email': {'required': "", "invalid": format_html('<div class="alert alert-danger alert-dismissible fade show" role="alert"> Ingresa una dirección de correo electrónico válida <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')},
            'cel': {'required': "", "max_length": format_html('<div class="alert alert-danger alert-dismissible fade show" role="alert"> Número de teléfono no válido. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')},
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.strip()) < 3:
            raise forms.ValidationError(format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> El nombre debe tener al menos 3 caracteres. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))
        return name

