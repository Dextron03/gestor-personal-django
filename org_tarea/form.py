from django import forms
from . import models
from django.utils.html import format_html


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        
        labels={
            "title":"Titulo de la tarea",
            "description":"Descripcion",
            "date_completion":"Fecha",
            "hour_completion":"Hora"
            }
        
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control", "placeholder":"Titulo de la tarea"}),
            "description":forms.Textarea(attrs={"class":"form-control", "placeholder":"¿Algun apunte?"}),
            "priority":forms.NumberInput(attrs={"class":"form-control", "style":"width:100px;"}),
            "date_completion":forms.DateInput(attrs={"class":'form-control',"style":"width:200px;" ,"type":"date"}),
            "hour_completion":forms.TimeInput(attrs={"class":"form-control", "style":"width:200px;","type":"time"}),
            }
        
        error_messages = {
            "title":{"required":""},
            "hour_completion":{"required":"", 'invalid':format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> La hora que ingresaste no es valida. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')},
            "priority":{"required":"",'invalid': format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Ingresa un número entero válido <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')}
        }

    def clean_priority(self):
        priority = self.cleaned_data.get("priority")
        if priority > 3 or priority < 1:
            raise forms.ValidationError(format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert"> Numero de prioeidad invalido. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'))
        return priority
            