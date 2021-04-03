import uuid
from django.db import models
from django.contrib.auth.models import User

from plans.models import Plan


class MyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plans = models.ManyToManyField(Plan, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
