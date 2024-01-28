from django.db import models
from datetime import datetime

class Students(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    address = models.CharField(max_length=255, verbose_name="Address")
    phone = models.CharField(max_length=255, verbose_name="Phone Number")
    email = models.EmailField(max_length=254, verbose_name="Email Address")
    date_registered = models.DateField(default=datetime.now())

    def __str__(self):
        return (f'{self.first_name} {self.last_name} is registered. {self.date_registered}')