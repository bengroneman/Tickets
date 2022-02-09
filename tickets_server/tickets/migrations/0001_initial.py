# Generated by Django 3.2.11 on 2022-02-08 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('summary', models.CharField(default='No Summary Provided', max_length=500)),
                ('status', models.CharField(choices=[('open', 'Open'), ('wip', 'Work in Progress'), ('pend', 'Pending'), ('cancel', 'Cancelled'), ('complete', 'Completed'), ('closed', 'Closed')], default='open', max_length=20)),
                ('assignee', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.person')),
            ],
        ),
    ]
