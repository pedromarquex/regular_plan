import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from patterns.choices import CYCLE_CHOICES, TYPE_CHOICES, UNIT_CHOICES


class RegularPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    tar_included = models.BooleanField()
    subscription = models.FloatField()
    cycle = models.CharField(max_length=10, choices=CYCLE_CHOICES)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    offer_iva = models.BooleanField()
    off_peak_price = models.FloatField()
    peak_price = models.FloatField()
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    valid = models.BooleanField()
    publish = models.BooleanField()
    vat = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plans = models.ManyToManyField(RegularPlan)

    def __str__(self):
        return self.user.username

