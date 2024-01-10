from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("add_contact/", views.contact_form, name="add_contact"),
    path("detailed/<int:id>/", views.info_detailed, name='detailed'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path("edit/<int:id>/", views.edit_contact, name="edit_contact"),
    path("", views.index, name="home_contact")
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
