# from django.http import JsonResponse
   
from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response

from energy.models import Building, Meter, Halfhourly
from django.db.models import Sum, Avg

import time
   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'insight/index.html')


def getTotalConsumptionHotel(unit_type):

    print('Computing average consumption per hotel ...')
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

    data = hotels.values()

    print(time.time() - start, 'seconds for computing total consumption per hotel')

    legend = 'Total Consumption per Hotel in 2018 ('+ unit_type +')'
    return labels, data, legend


def getAvgConsumptionTime(unit_type):

    print('Computing average consumption per hour ...')
    start = time.time()

    # Making a dictionary for reference to hours
    options_hours = [x for x in range(0, 24)]
    options_minutes = [0, 30]

    labels = []
    data = []

    for h in options_hours:
        for m in options_minutes:
            # Compute consumption average per hour, minute combination
            out = Halfhourly.objects.filter(meter_id__unit__contains=unit_type)\
                                    .filter(reading_date_time__hour__in=[h])\
                                    .filter(reading_date_time__minute__in=[m])\
                                    .aggregate(Avg('consumption'))
            out = float(out['consumption__avg'])
            data.append(out)

            # Formatting corresponding time labels
            t = [h, m]
            for i in range(len(t)):
                t[i] = str(t[i])
                if len(t[i]) == 1: t[i] = '0'+t[i]
            t = t[0] + ':' + t[1]
            labels.append(t)

    print(time.time() - start, 'seconds for computing average consumption per hour')

    legend = 'Average Consumption per Half Hour End in 2018 ('+ unit_type +')'
    return labels, data, legend 


# Making it a global scope so it is only computed once
hotel_cons_labels, hotel_cons_data, hotel_cons_legend = getTotalConsumptionHotel('kWh')  
time_cons_labels, time_cons_data, time_cons_legend = getAvgConsumptionTime('kWh') 


## using rest_framework classes
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):

        # Preparing body to send to ChartJS
        body ={
            'hotel_cons_legend': hotel_cons_legend,
            'hotel_cons_labels': hotel_cons_labels,
            'hotel_cons_data': hotel_cons_data,
            'time_cons_legend': time_cons_legend,
            'time_cons_labels': time_cons_labels,
            'time_cons_data': time_cons_data,
        }
        return Response(body)