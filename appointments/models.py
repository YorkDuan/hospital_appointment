from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    bio = models.TextField()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)
