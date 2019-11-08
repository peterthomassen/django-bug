import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


def uuid_hex():
    return uuid.uuid4().hex


class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, max_length=32, default=uuid_hex, editable=False)
    email = models.EmailField(max_length=191, unique=True)

    USERNAME_FIELD = 'email'


class Domain(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='domains')

