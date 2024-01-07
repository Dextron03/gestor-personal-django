from django.urls import path
from . import views

urlpatterns = [
    path("GestForm/", views.contact_form, name="GestForm")
    
]
