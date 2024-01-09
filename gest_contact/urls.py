from django.urls import path
from . import views

urlpatterns = [
    path("GestForm/", views.contact_form, name="GestForm"),
    path("detailed/<int:id>/", views.info_detailed, name='detailed'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path("edit/<int:id>/", views.edit_contact, name="edit_contact"),
    path("", views.index, name="home_contact")
    
]
