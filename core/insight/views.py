# from django.http import JsonResponse
   
from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response

from energy.models import Building, Meter, Halfhourly

import time
   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'insight/index.html')


def getTotalConsumption(unit_type):

    print('Computing total consumption ...')
    start = time.time()

    # Making a dictionary for reference to hotel building names
    hotels = list(map(lambda o: o.name, Building.objects.all()))
    hotels = dict([(key, 0) for key in hotels])

    # Summing consumption in total for objects in kWH
    filtered = Halfhourly.objects.filter(meter_id__unit__contains=unit_type)
    for h in filtered:
        hotels[h.meter_id.building_id.name] += float(h.consumption)

    labels = list(hotels)
    chartdata = hotels.values()

    print(time.time() - start, 'seconds for computing total consumption per hotel')

    chartlegend = 'Total consumption per Hotel in 2018 ('+ unit_type +')'
    return labels, chartdata, chartlegend

labels, chartdata, chartlegend = getTotalConsumption('kWh')  # Making it a constant so it doesnt need to be computed every time
   
## using rest_framework classes
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):

        # Preparing body to send to ChartJS
        body ={
            'chartlegend': chartlegend,
            'labels': labels,
            'chartdata': chartdata
        }
        return Response(body)