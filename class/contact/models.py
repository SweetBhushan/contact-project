from django.db import models

# Create your models here.
class ContactModel(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=50)
	#discription=models.TextField(max_length=100)
	