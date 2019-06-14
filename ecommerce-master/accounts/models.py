from django.contrib.auth.models import User
from django.db import models

class GuestEmail(models.Model):
    email     = models.EmailField()
    active    = models.BooleanField(default=True)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class User2(models.Model):
    user  = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user)
