from django.contrib import admin
from . import models
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','note','email')
    search_fields=('name','cel')
    list_filter = ['date', 'name']
    # date_hierarchy = "date" 
    
admin.site.register(models.Contact, ContactAdmin)

