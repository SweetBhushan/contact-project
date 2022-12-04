from django.contrib import admin

from .models import ContactModel


# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','address','phone']
admin.site.register(ContactModel,contactAdmin)