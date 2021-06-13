from django.shortcuts import render
from django.views import generic

from .models import Building

# Create your views here.
class BuildingView(generic.ListView):
    template_name = 'energy/building.html'
    context_object_name = 'building_list'

    def get_queryset(self):
        return Building.objects.all()