from django.shortcuts import render, redirect
from . import form
from . import models
from django.contrib import messages
from django.utils.html import format_html
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
        form_edit_contact = form.ContactForm(request.POST, request.FILES, instance=contact_edit)
        if form_edit_contact.is_valid():
            form_edit_contact.save()
            messages.success(request, "El contacto a sido actulizado correctamente.")
            return redirect("home_contact")
        return render(request, "gest_contact/contact_edit.html", {"form":form_edit_contact, "id":id})

def delete_contact(request, id):
    contacts = models.Contact.objects.get(id = id)
    if request.method == "GET":
        contacts.delete()
        messages.success(request, "El contacto a sido eliminado")
        return redirect("home_contact")
    return render(request, "gest_contact/index.html", {"info":contacts})
    
    

def contact_form(request):
    if request.method == "GET":
        form_contact = form.ContactForm()
        return render(request, "gest_contact/contact_form.html", {"form":form_contact})
    
    if request.method == "POST":
        form_contact = form.ContactForm(request.POST, request.FILES)
        if form_contact.is_valid():
            form_contact.save()
            messages.success(request, format_html(f"El contacto <strong>{form_contact.cleaned_data['name']}</strong> se ha creado exitosamente."))
            return render(request, "gest_contact/contact_form.html", {"form": form_contact})
        else:
            return render(request, "gest_contact/contact_form.html", {"form": form_contact})
    

