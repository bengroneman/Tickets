from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TicketSerializer, PersonSerializer
from .models import Ticket, Person


@api_view(['GET', 'POST'])
def ticket_collection(request):
    """
    List all tickets
    """
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        person = {
            'email': request.data['email'],
            'full_name': request.data['full_name']
        }
        person_serializer = PersonSerializer(data=person)
        person_valid = person_serializer.is_valid()
        if person_valid:
            person_serializer.save()
        
        ticket_serializer = TicketSerializer(data=request.data)
        ticket_valid = ticket_serializer.is_valid()
        if ticket_valid:
            ticket_serializer.save()
            return Response((ticket_serializer.data, person_serializer.data), status=200)
        return Response((ticket_serializer.errors, person_serializer.errors), status=400)


@api_view(['GET', 'DELETE'])
def ticket_element(request, pk):
    """
    Retrieve, update or delete a ticket instance.
    """
    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        ticket.delete()
        return HttpResponse(status=204)

