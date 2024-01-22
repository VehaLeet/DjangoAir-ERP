from django.db import models
from users.models import CustomUser


class Ticket(models.Model):
    flight = models.ForeignKey(
        "Flight",
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    check_in_status = models.BooleanField(default=False)
    boarding_status = models.BooleanField(default=False)
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tickets')
    seat = models.ForeignKey("AirplaneSeat", on_delete=models.CASCADE)
    options = models.OneToOneField(
        "Option",
        on_delete=models.CASCADE,
    )
    discount = models.IntegerField(choices=[(3, '3%'), (5, '5%'), (7, '7%')])
    code = models.CharField(max_length=10, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Flight(models.Model):
    number = models.IntegerField()
    destination = models.CharField(max_length=10, unique=True)
    flight_date = models.DateTimeField(null=True)
    airplane = models.OneToOneField(
        "Airplane",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Airplane(models.Model):
    model = models.CharField(max_length=10, unique=True, null=False)


class SeatType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()


class AirplaneSeat(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="seats")
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE, related_name="seat_types")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Option(models.Model):
    meal = models.BooleanField(default=False)
    luggage = models.BooleanField(default=False)
