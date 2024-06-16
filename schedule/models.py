from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import holidays

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



class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)    
    time = models.CharField(max_length=5, choices=[
        ('09:00', '09:00'), ('10:00', '10:00'), 
        ('11:00', '11:00'), ('12:00', '12:00'), 
        ('13:00', '13:00'), ('14:00', '14:00'), 
        ('15:00', '15:00'), ('16:00', '16:00'), 
        ('17:00', '17:00'), ('18:00', '18:00'), 
        ('19:00', '19:00'), ('20:00', '20:00'), 
    ])
    
    def save(self, *args, **kwargs):
        # Check if appointment already exists for the same date and time
        appointments = Schedule.objects.filter(date=self.date, time=self.time)
        if appointments.exists():
            raise ValidationError("Appointment already exists for the same date and time.")
        # Check if appointment falls on a weekend or bank holiday
        if self.date.weekday() > 4 or self.is_bank_holiday(self.date):
            raise ValidationError("Appointments are not available on weekends or bank holidays in Ireland.")
        super().save(*args, **kwargs)

    # Function to check if a date is a bank holiday in Ireland
    @staticmethod
    def is_bank_holiday(date):
        ireland_holidays = holidays.Ireland()
        if date.weekday() >= 5 or date in ireland_holidays:
             return True
        return False   

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.user} {self.date} {self.time}"    