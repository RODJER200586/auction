from django.contrib.auth.models import User
from django.db import models


class Lot(models.Model):
    OPENED = 'opened'
    CLOSED = 'closed'
    CANCELED = 'canceled'
    STATUS_CHOICES = (
        (OPENED, 'Opened'),
        (CLOSED, 'Closed'),
        (CANCELED, 'Canceled'),
    )
    name = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='lots/%Y/%m/%d/')
    start = models.DateTimeField()
    finish = models.DateTimeField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=OPENED)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
