from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email_address = models.EmailField(max_length=100)
    street = models.CharField(max_length=100)
    eircode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ['surname', 'forename']

    def __str__(self):
        return f"{self.forename} {self.surname}"
