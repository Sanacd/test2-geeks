from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactsForm

def contacts(request):
    form = ContactsForm()  # Create an instance of the form
    if request.method == "POST":
        form = ContactsForm(request.POST)  # Bind the form with the submitted data
        if form.is_valid():  # Validate the form
            form.save()  # Save the form data to the database

    return render(request, 'contact/contact.html', {'form': form})