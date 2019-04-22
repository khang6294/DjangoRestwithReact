from django.db import models

# Create your models here.

class DateData(models.Model):
    pub_date = models.DateField()
    total_messages = models.IntegerField()
    total_customers = models.IntegerField()

    def __str__(self):
        return self.pub_date.strftime('%Y-%m-%d')

        

