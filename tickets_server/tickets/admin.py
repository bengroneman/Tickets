from django.contrib import admin
from .models import Ticket, Person


class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'subject', 'summary', 'status', 'email', 'urgency', 'bucket')
    list_filter = ('status', 'bucket')
    search_fields = ('ticket_number', 'summary', 'subject')
    ordering = ('status', 'urgency', 'bucket')
    pass


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'title')
    pass


admin.site.register(Person, PersonAdmin)

admin.site.register(Ticket, TicketAdmin)



