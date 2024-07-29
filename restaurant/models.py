from django.db import models
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=200)
    reservation_date = models.DateField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        ordering = ['reservation_date', 'reservation_slot']

    def __str__(self): 
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f'{self.title}: ${self.price:.2f}'

