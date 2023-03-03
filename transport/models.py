from django.db import models

# Create your models here.
class Farmer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.TextField()
    mobile=models.CharField(max_length=15)
    location=models.CharField(max_length=200)
    supply_capacity=models.FloatField()

class Driver(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.TextField()
    mobile=models.CharField(max_length=15)
    rides_made=models.IntegerField()
    rating=models.IntegerField()
    license_no=models.IntegerField()

class Truck(models.Model):
    make=models.CharField(max_length=100)
    model=models.CharField(max_length=200)
    registration_no=models.CharField(max_length=200)
    capacity=models.IntegerField()
    prime_location=models.CharField(max_length=200)
    insured=models.BooleanField()

class BookingDetails(models.Model):
    farmer_id=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    truck_id=models.ForeignKey(Truck,on_delete=models.CASCADE)
    driver_id=models.ForeignKey(Driver,on_delete=models.CASCADE)
    source=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    time_of_request=models.DateField(auto_now=True)
    status=models.CharField(max_length=10)

class PaymentDetails(models.Model):
    booking_id=models.ForeignKey(BookingDetails,on_delete=models.CASCADE)
    amount=models.FloatField()
    mode_of_payment=models.CharField(max_length=100)