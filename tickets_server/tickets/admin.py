from django.contrib import admin
from .models import Ticket, Person


class TicketAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)

admin.site.register(Ticket, TicketAdmin)



