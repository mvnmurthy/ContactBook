from django.db import models
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField

class Contacts(models.Model):
	""" Contact book model """
	first_name = models.CharField(max_length=255, blank=False)
	last_name = models.CharField(max_length=255, blank=False)
	phone_number = PhoneNumberField(blank = False)
	email = models.EmailField(max_length=100, blank = False, unique = True, validators=[validate_email])
	city = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add = True)
	date_modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{0} {1}".format(self.first_name, self.last_name)
