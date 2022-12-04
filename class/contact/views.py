from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView, RedirectView
from .models import ContactModel
from .form import ContactForm

# Create your tests here.
class ContactCreate(TemplateView):
	template_name ='contact/contact_form.html'
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(**kwargs)
		fm = ContactForm()
		context={'form':fm}
		return context
     
	def post (self,request):
		fm= ContactForm(request.POST)
		if fm.is_valid():
			fm.save()
		return HttpResponseRedirect('/contacts/')	


class ContactList(ListView):
	model=ContactModel
	template_name= 'contact/contact_list.html'
	context_object_name= 'ContactModel'

class ContactDetail(DetailView):
	model = ContactModel
	template_name= 'contact/contact_datail.html'

class ContactUpdate(UpdateView):
	model = ContactModel
	fields=['name','email','address','phone']
	success_url='/contacts/'
	template_name= 'contact/contact_update.html'

class ContactDelete(DeleteView):
	model = ContactModel
	template_name= 'contact/contact_delete.html'
	success_url= '/contacts/'
		








	
