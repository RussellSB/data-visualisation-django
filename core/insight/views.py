# from django.http import JsonResponse
   
from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response

from energy.models import Building, Meter, Halfhourly
from django.db.models import Sum, Q

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
    labels = []

    for hotel in hotels:        
        # Compute consumption sum per hotel
        out = Halfhourly.objects.filter(meter_id__building_id__name__contains=hotel)\
                                .filter(meter_id__unit__contains=unit_type)\
                                .aggregate(Sum('consumption'))
        out = float(out['consumption__sum'])
        hotels[hotel] = out

        # Remove brackets segment if present in string name
        if '(' in hotel: 
            labels.append(hotel.split('(')[0])
        else: 
            labels.append(hotel)

    chartdata = hotels.values()

    print(time.time() - start, 'seconds for computing total consumption per hotel')

    chartlegend = 'Total consumption per Hotel in 2018 ('+ unit_type +')'
    return labels, chartdata, chartlegend

hotel_cons_labels, hotel_cons_data, hotel_cons_legend = getTotalConsumption('kWh')  # Making it a constant so it doesnt need to be computed every time a request is sent
   
## using rest_framework classes
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):

        # Preparing body to send to ChartJS
        body ={
            'hotel_cons_legend': hotel_cons_legend,
            'hotel_cons_labels': hotel_cons_labels,
            'hotel_cons_data': hotel_cons_data
        }
        return Response(body)