import uuid
from django.db import models
from django.contrib.auth.models import User

from plans.models import Plan


class MyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plans = models.ManyToManyField(Plan)

    def __str__(self):
        return self.user.username

