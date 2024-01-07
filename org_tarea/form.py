from django import forms
from . import models

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
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "date_completion":forms.DateInput(attrs={"class":'form-control', "type":"date"}),
            "hour_completion":forms.TimeInput(attrs={"class":"form-control", "type":"time"})
            }