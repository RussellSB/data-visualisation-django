from django.urls import path
from . import views

app_name = 'insight'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('api', views.ChartData.as_view()),
]