from django import forms
from . import models
from django.utils.html import format_html

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control",'placeholder':"Nombre del contacto"}),
                   "surnames":forms.TextInput(attrs={"class":"form-control"}),
                   "note":forms.Textarea(attrs={"class":"form-control"}),
                   "cel":forms.NumberInput(attrs={"class":"form-control"}),
                   "email":forms.EmailInput(attrs={"class":"form-control"}),
                   }
        
        labels = {"name":"Nombres",
                  "surnames":"Apellidos",
                  "note":"nota",
                  "cel":"Celular"}
        
        error_messages = {
            'name': {'required': ("")},
            'email': {'required': ("")},
            'cel': {'required': ("")},
            }

    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError(format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> El nombre debe tener al menos 3 caracteres. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))
        return name
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
        
        