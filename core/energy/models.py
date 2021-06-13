from django.db import models

class Building(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('the hotel building name', max_length=50)

    def __str__(self):
        return '{}, {}'.format(self.id,self.name)

class Meter(models.Model):
    id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    fuel = models.CharField('the type of fuel', max_length=50)
    unit = models.CharField('the unit of the fuel type', max_length=50)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.id, self.building_id.id, self.fuel, self.unit)

class Halfhourly(models.Model):
    meter_id = models.ForeignKey(Meter, on_delete=models.CASCADE)
    consumption = models.DecimalField('the fuel consumption within the past half hour', max_digits=20, decimal_places=4)
    reading_date_time = models.DateTimeField('the end time of the half hour duration')

    def __str__(self):
        date_time_str = self.reading_date_time.__str__()
        return '{}, {}, {}, {}'.format(self.id, self.meter_id.id, date_time_str, self.consumption)

