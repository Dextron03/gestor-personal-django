from django.shortcuts import render
from . import form

# Create your views here.
def contact_form(request):
    if request.method == "GET":
        form_contact = form.ContactForm(request.GET)
        return render(request, "forms/contact_form.html", {"form":form_contact})
    
    if request.method == "POST":
        form_contact = form.ContactForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return render(request, "forms/contact_form.html", {"form":form_contact})
        else:
            return render(request, "error.html", {})

