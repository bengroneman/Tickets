from django.urls import path
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^api/v1/tickets/$', views.ticket_collection),
    url(r'^api/v1/tickets/(?P<pk>[0-9]+)$', views.ticket_element)
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
