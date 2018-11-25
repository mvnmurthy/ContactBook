from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import CreateView, DetailsView

#router = routers.DefaultRouter()
#router.register(r'contactlist', CreateView)


urlpatterns = {
	url(r'^$', CreateView.as_view(), name= "create"),
	url(r'^(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
	url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
}

urlpatterns = format_suffix_patterns(urlpatterns)