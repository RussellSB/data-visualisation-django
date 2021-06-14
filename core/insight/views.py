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
        buildings = Building.objects.all()
        labels = ['a', 'b', 'c'] #list(map(lambda o: o.name, buildings))
        chartdata = [1,2,3] #list(map(lambda o: o.id, buildings))

        data ={
            'chartLabel': 'my data',
            'labels': labels,
            'chartdata': chartdata
        }
        return Response(data)