from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_quest = models.PositiveBigIntegerField()
    booking_date = models.DateTimeField

    def __str__(self):
        return f"{self.name} - {self.booking_date} - {self.no_of_quest}"
        