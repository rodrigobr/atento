from django.db import models

# Create your models here.

class Contacts(models.Model):
    name  = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField(required=False)
    description = models.TextField()

