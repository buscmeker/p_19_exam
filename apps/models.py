from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=155)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField()