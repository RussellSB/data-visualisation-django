from django.shortcuts import render
from .forms import CsvModelForm
import datetime
import csv

from energy.models import Building, Meter, Halfhourly

# Knowing which model to load rows into by this simple reference list
CSVS = ['building_data.csv', 'meter_data.csv', 'halfhourly_data.csv']

# Create your views here.
def upload_csv(request):
    form = CsvModelForm(request.POST, request.FILES)
    csv_filename = str(request.FILES['file_name']) if form.is_valid() else None 

    # Only process if form is valid and filename matches what is expected
    if csv_filename is not None and csv_filename in CSVS:
        obj = form.save()

        # Loads CSV and iterates through each row for parsing
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i > 0:  # Ignore first row as it is column description

                    # Skips rows with empty first column entries as a precaution
                    if len(row[0]) == 0: continue  

                    if csv_filename == CSVS[0]: parse_building(row)
                    elif csv_filename == CSVS[1]: parse_meter(row)
                    elif csv_filename == CSVS[2]: parse_halfhourly(row)

        obj.activated = True
        obj.save()
    return render(request, 'csvs/upload.html', {'form': form})


def parse_building(row):
    Building.objects.create(id=row[0], name=row[1])

def parse_meter(row):
    building_ref = Building.objects.get(pk=row[0])  # refers to other datatable
    Meter.objects.create(building_id=building_ref, id=row[1], fuel=row[2], unit=row[3])

def parse_halfhourly(row):
    # Constructs datetime object from parsed string
    date_time_spl = row[2].split(' ')
    date = date_time_spl[0]
    date_spl = [int(x) for x in date.split('-')]
    time = date_time_spl[1]
    time_spl = [int(x) for x in time.split(':')]

    date_time = datetime.datetime(
                    year=date_spl[0], 
                    month=date_spl[1], 
                    day=date_spl[2], 
                    hour=time_spl[0], 
                    minute=time_spl[1], 
                    second=0,
                )

    meter_ref = Meter.objects.get(pk=row[1]) # refers to other datatable
    Halfhourly.objects.create(consumption=row[0], meter_id=meter_ref, reading_date_time=date_time)