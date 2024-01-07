from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.org_task, name="todo")
]
