from django.db import models

# Create your models here.
class ModeOfPayment(models.Model):
    mode_of_payment = models.CharField(max_length=20)

    def __str__(self):
        return self.mode_of_payment

    class Meta:
        verbose_name = 'Mode Of Payment'
        db_table =  'tbl_Mode_Of_Payment'