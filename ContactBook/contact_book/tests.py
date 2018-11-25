from django.test import TestCase
from django.contrib.auth.models import User
from .models import Contacts
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ContactsTestCase(TestCase):
	def setUp(self):
		self.first_name = "Mantha"
		self.last_name = "Murthy"
		self.email = "manthavnmurthy@gmail.com"
		self.phone_number = "8884394443"
		self.city = "Raipur"
		self.contact = Contacts(
					first_name = self.first_name, 
					last_name = self.last_name,
					email = self.email,
					phone_number = self.phone_number,
					city = self.city,
				)

	def test_model_can_create_contact_list(self):
		""" Test whether a record can be inserted """
		old_count = Contacts.objects.count()
		self.contact.save()
		new_count = Contacts.objects.count()
		self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		user = User.objects.create(username='admin')
		user.set_password('admin')
		user.save()
		self.client.login(username='admin', password='admin')
	
		self.contact_data = {
							  'first_name':'Appu', 
							  'last_name': 'Mantha',
							  'email': 'appu123@gmail.com',
							  'phone_number':'+911234567890',
							  'city':'Raipur',
         					}
		self.response = self.client.post(reverse('create'),	self.contact_data, format = "json")
		
	def test_api_can_create_a_contact(self):
		""" Test whether create contact api works """
		self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_retrive_a_contact(self):
		""" Test whether api can get a contact"""
		contact_list = Contacts.objects.get()
		response = self.client.get(reverse('details', kwargs={'pk': contact_list.id}), format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['first_name'], contact_list.first_name)

	def test_api_can_update_a_contact(self):
		""" Test whether api can update a contact """
		contact_list = Contacts.objects.get()
		update_contact_list = { 'first_name':'Murthy'}
		response = self.client.patch(
				reverse('details', kwargs={'pk': contact_list.id}),
				update_contact_list, format='json'
			)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_api_can_delete_a_contactlist(self):
		""" Test whether the api can delete a contact. """
		contactlist = Contacts.objects.get()
		response = self.client.delete(
				reverse('details', kwargs={'pk': contactlist.id} ),
				format = 'json',
				follow=True)
			
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
