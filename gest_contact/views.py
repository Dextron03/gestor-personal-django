from django.shortcuts import render
from . import form
from . import models

# Create your views here.
def index(request):
    # ! busca el elemento que fue escrito en la barra de navegacion
    inf_contacts = models.Contact.objects.filter(name__contains = request.GET.get('search', ""))
    
    return render(request, "gest_contact/index.html", {"info":inf_contacts})

def info_detailed(request, id):
    inf_contacts = models.Contact.objects.get(id = id) 
    return render(request, "gest_contact/contact_detailed.html", {"info":inf_contacts})

def edit_contact(request, id):
    contact_edit = models.Contact.objects.get(id=id)
    if request.method == "GET":
        form_edit_contact = form.ContactForm(instance=contact_edit)
        return render(request, "gest_contact/contact_edit.html", {"form":form_edit_contact, "id":id})
        
    
    if request.method == "POST":
        form_edit_contact = form.ContactForm(request.POST, instance= contact_edit)
        if form_edit_contact.is_valid():
            form_edit_contact.save()
            return render(request, "gest_contact/contact_edit.html", {"form":form_edit_contact, "id":id})


def contact_form(request):
    if request.method == "GET":
        form_contact = form.ContactForm(request.GET)
        return render(request, "gest_contact/contact_form.html", {"form":form_contact})
    
    if request.method == "POST":
        form_contact = form.ContactForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return render(request, "gest_contact/contact_form.html", {"form":form_contact})
        else:
            return render(request, "error.html", {})

