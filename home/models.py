from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()
    def __str__(self):
        return self.dep_name

class Mechanic(models.Model):
    mech_name = models.CharField(max_length=100)
    mech_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
    mech_img=models.ImageField(upload_to='Mechanics')

class Booking(models.Model):
    c_name=models.CharField(max_length=255)
    c_phone= models.CharField(max_length=100)
    c_email= models.EmailField()
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
