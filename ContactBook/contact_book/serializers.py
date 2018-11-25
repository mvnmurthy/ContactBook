from rest_framework import serializers
from .models import Contacts

class ContactlistSerializer(serializers.ModelSerializer):
	""" Serializer class for the Contacts model """
	class Meta:
		model = Contacts
		fields = ("first_name", "last_name", "phone_number", "email", "city", "date_created", "date_modified")
		read_only_fields = ("date_created", "date_modified")

