from django.contrib import admin
from . import models
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    pass 

admin.site.register(models.Contact, ContactAdmin)