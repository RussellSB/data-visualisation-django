from django.urls import path
from . import views

app_name = 'energy'
urlpatterns = [
    path('building/', views.BuildingView.as_view(), name='building'),
    path('building/<int:pk>/', views.BuildingSpecificView.as_view(), name='building_specific'),
    path('meter/', views.MeterView.as_view(), name='meter'),
    path('meter/<int:pk>/', views.MeterSpecificView.as_view(), name='meter_specific'),
    path('halfhourly/', views.HalfHourlyView.as_view(), name='halfhourly')
]
