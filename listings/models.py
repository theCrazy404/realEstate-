from django.db import models

from datetime import datetime

class Listing(models.Model):
     title = models.CharField(max_length= 200)
     address = models.CharField(max_length=200)
     city = models.CharField(max_length=20)
     state = models.CharField(max_length=50)
     zipcode = models.CharField(max_length=20)
     description = models.TextField(blank=True)
     price = models.IntegerField()
     bedrooms = models.IntegerField()
     garage = models.DecimalField(max_digits= 5,decimal_places= 1)
     sqft = models.IntegerField()
     photo_main = models.ImageField(upload_to= 'photo/%Y/%m/%d/')
     photo_1 = models.ImageField(upload_to= 'photo/%Y/%m/%d/',blank= True)
     photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
     photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
     photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
     photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True);
     photo_6 = models.ImageField(upload_to= 'photo/%Y/%m/%d/',blank= True)
     is_published = models.BooleanField(default =  True)
     list_date = models.DateTimeField(default= datetime.now,blank= True)
     def __str__(self):
         return self.title


