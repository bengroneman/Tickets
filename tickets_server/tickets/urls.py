from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    re_path(r'^api/tickets/$', views.ticket_collection),
    re_path(r'^api/tickets/(?P<pk>[0-9]+)$', views.ticket_element)
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
