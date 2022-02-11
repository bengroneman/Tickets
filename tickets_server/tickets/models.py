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
    URGENCY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    BUCKET_CHOICES = [
        ('quality', 'Quality'),
        ('engineering', 'Engineering'),
        ('unassigned', 'Unassigned'),
    ]
    ticket_number = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=100, default="NO Subject")
    summary = models.CharField(max_length=500, default="NO Summary")
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    bucket = models.CharField(choices=BUCKET_CHOICES, max_length=20, default='unassigned')
    urgency = models.CharField(choices=URGENCY_CHOICES, max_length=10, default='low')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='open', max_length=20)
