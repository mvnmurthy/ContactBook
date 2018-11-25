from rest_framework import generics, filters
from .serializers import ContactlistSerializer
from .models import Contacts
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CreateView(generics.ListCreateAPIView):
	""" This class defines the create behavior of our rest api. """
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = Contacts.objects.all()
	serializer_class = ContactlistSerializer

	def perform_create(self, serializer):
		""" Save the post data when creating a new contact list """
		serializer.save()

	def get_queryset(self):
		queryset = Contacts.objects.all()
		first_name = self.request.query_params.get('first_name', None)
		if first_name is not None:
			queryset = queryset.filter(first_name=first_name)
	
		email = self.request.query_params.get('email', None)
		if email is not None:
			queryset = queryset.filter(email=email)

		return queryset


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	""" This class handles the http GET, PUT and DELETE requests. """
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	queryset = Contacts.objects.all()
	serializer_class = ContactlistSerializer