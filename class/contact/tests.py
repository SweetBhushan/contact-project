from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
# Create your tests here.
class ContactList(ListView): 
	model = Contact

class ContactDetail(DetailView): 
	model = Contact

class ContactCreate(CreateView): 
	model = Contact

class ContactUpdate(UpdateView): 
	model = Contact

class ContactDelete(DeleteView): 
	model = Contact    