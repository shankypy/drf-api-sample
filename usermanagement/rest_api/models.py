from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=250)
    task_progress = models.PositiveIntegerField(default=0)
    user = models.ManyToManyField(User, blank=True)
    group = models.ManyToManyField(Group, blank=True)