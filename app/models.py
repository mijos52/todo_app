from datetime import date
from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateField()