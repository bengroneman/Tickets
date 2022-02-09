# https://www.django-rest-framework.org/api-guide/serializers/#handling-saving-related-instances-in-model-manager-classes
# Helpful reference ^
from django.http import HttpResponse
from rest_framework import serializers
from .models import Ticket, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

    def create(self, validated_data):
        return Person.objects.create(**validated_data)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('__all__')

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

