from django.db import models

# Create your models here.
class Building(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('the hotel building name', max_length=50)

class Meter(models.Model):
    id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    fuel = models.CharField('the type of fuel', max_length=50)
    unit = models.CharField('the unit of the fuel type', max_length=50)

class Halfhourly(models.Model):
    meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
    consumption = models.DecimalField('the fuel consumption within the past half hour')
    reading_date_time = models.DateTimeField('the end time of the half hour duration')

