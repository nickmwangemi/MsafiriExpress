from django.db import models

# Create your models here.
class Bus(models.Model):
    type =  models.CharField(max_length=100)
    reg_number = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()


    def __str__(self):
            return self.type
    
    class Meta:
        verbose_name_plural = 'Buses'
        db_table = 'tbl_Bus'
