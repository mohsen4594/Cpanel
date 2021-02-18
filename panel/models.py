from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class proplem (models.Model):
    name=models.CharField(max_length=255)
    date=models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
