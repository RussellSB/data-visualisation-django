from django.urls import path
from . import views

app_name = 'energy'
urlpatterns = [
    path('building', views.BuildingView.as_view(), name='building')
]
