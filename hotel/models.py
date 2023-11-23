from django.db import models
from django.conf import settings


# Create your models here.


class Room(models.Model):
    ROOM_CATEGORIES=(
        ('A25', 'Apt A25 1 Bedroom'),
        ('A01', 'Apt A01 2 Bedrooms'),
        ('A19', 'Apt A19 2 Bedrooms'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField( )

    def __str__(self):
        return f'{self.number}. Apartment {self.category} with {self.beds} beds for a max number of {self.capacity}  people' 
    
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

