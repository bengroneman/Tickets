from django.contrib import admin
from .models import Ticket, Person
from .serializers import TicketSerializer


class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'subject', 'summary', 'status', 'email', 'urgency', 'bucket')
    list_filter = ('status', 'bucket')
    search_fields = ('ticket_number', 'summary', 'subject')
    ordering = ('status', 'urgency', 'bucket')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        ticket_query = Ticket.objects.values()
        tickets = [ticket for ticket in ticket_query]
        extra_context['tickets'] = tickets
        return super(TicketAdmin, self).changelist_view(request, extra_context=extra_context)
    pass


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'title')
    pass


admin.site.register(Person, PersonAdmin)

admin.site.register(Ticket, TicketAdmin)
