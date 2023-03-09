import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(max_length=200, unique=True)
    firstname = models.CharField(max_length=100, blank=True, default="")
    lastname = models.CharField(max_length=100, blank=True, default="")

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}: {self.firstname} {self.lastname}"
