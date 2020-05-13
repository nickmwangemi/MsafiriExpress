from django.db import models
from datetime import datetime,time
from buses.models import Bus

# Create your models here.
class TravelRoute(models.Model):
    title = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date_of_travel= models.DateTimeField(default=datetime.now, blank=True)
    time_of_departure = models.TimeField()
    bus_type = models.ForeignKey(Bus,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    price = models.IntegerField()

    def __str__(self):
            return self.title
    
    class Meta:
        db_table = 'tbl_TravelRoutes'