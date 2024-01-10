from django.urls import path
from . import views

urlpatterns = [
    path("add_task/", views.add_task, name="add_task"),
    path("delete/<int:id>/", views.detele_task, name="delete_task"),
    path("edit_task/<int:id>", views.edit_task, name="edit_task"),
    path("", views.index, name="home_tasks")
]
