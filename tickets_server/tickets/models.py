from django.db import models
from django.contrib.auth.models import User

# TODO: consider new name for this (Reporter?)
class Person(models.Model):
    email = models.EmailField(primary_key=True)
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11, blank=True)


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('wip', 'Work in Progress'),
        ('pend', 'Pending'),
        ('cancel', 'Cancelled'),
        ('complete', 'Completed'),
        ('closed', 'Closed'),
    ]
    ticket_number = models.BigAutoField(primary_key=True)
    summary = models.CharField(max_length=500, default="No Summary Provided")
    # TODO: consider this naming scheme
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='open', max_length=20)
