# from django.http import JsonResponse
   
from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response

from energy.models import Building, Meter, Halfhourly
   
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'insight/index.html')
   
## using rest_framework classes
   
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        # Preparing data to visualise
        buildings = Building.objects.all()
        meters = Meter.objects.all()

        # Making a dictionary for reference to hotel building names
        hotels = list(map(lambda o: o.name, buildings))
        hotels = dict([(key, 0) for key in hotels])

        # Summing consumption in total for objects in kWH
        for i, h in enumerate(Halfhourly.objects.all()):
            m = h.meter_id

            if m.unit == 'kWh':
                hotels[m.building_id.name] += float(h.consumption)

            if i > 3000: break

        labels = list(hotels) #list(map(lambda o: o.name, buildings))
        chartdata = hotels.values()

        # Preparing body to send to ChartJS
        body ={
            'chartlegend': 'Total consumption per Hotel in 2018 (kWh)',
            'labels': labels,
            'chartdata': chartdata
        }
        return Response(body)