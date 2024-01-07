from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        
        widgets = {"name":forms.TextInput(attrs={"class":"form-control"}),
                   "surnames":forms.TextInput(attrs={"class":"form-control"}),
                   "cel":forms.NumberInput(attrs={"class":"form-control"}),
                   "email":forms.EmailInput(attrs={"class":"form-control"}),
                   }
        
        labels = {"name":"Nombres",
                  "surnames":"Apellidos",
                  "cel":"Celular"}