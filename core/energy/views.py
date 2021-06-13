from django.shortcuts import render
from django.views import generic

from .models import Building, Halfhourly, Meter

MAX = 200  # Max number of rows to display

# Create your views here.
class BuildingView(generic.ListView):
    template_name = 'energy/building.html'
    context_object_name = 'building_list'

    def get_queryset(self):
        return Building.objects.all()[:MAX]

class BuildingSpecificView(generic.DetailView):
    model = Building
    template_name = 'energy/building_specific.html'

class MeterView(generic.ListView):
    template_name = 'energy/meter.html'
    context_object_name = 'meter_list'

    def get_queryset(self):
        return Meter.objects.all()[:MAX]

class MeterSpecificView(generic.DetailView):
    model = Meter
    template_name = 'energy/meter_specific.html'

    
class HalfHourlyView(generic.ListView):
    template_name = 'energy/halfhourly.html'
    context_object_name = 'halfhourly_list'

    def get_queryset(self):
        return Halfhourly.objects.all()[:MAX]