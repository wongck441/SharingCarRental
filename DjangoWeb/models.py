from django.db import models
# Create your models here.
import datetime
import os

class Profile(models.Model):
   username = models.CharField(max_length=255)
   email = models.EmailField(max_length=255, null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)

   def __str__(self):
        return self.username

class Content(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    message_created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

class RentCar(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=8, null=True)
    email = models.EmailField(max_length=255, null=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_date = models.DateField(max_length=255, blank=True, null=True)
    dropoff_date = models.DateField(max_length=255, blank=True, null=True)
    pickup_time = models.TimeField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, null=True)
    rent_number = models.CharField(max_length=255)
    order_date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class BorrowCar(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    Car_Id = models.CharField(max_length=255)
    Car_Name = models.CharField(max_length=255)
    Car_Description = models.CharField(max_length=255)
    Car_Rental_Price = models.CharField(max_length=255)
    CarImage = models.ImageField(upload_to=filepath, null=True, blank=True)
    Car_borrow_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Car_Id