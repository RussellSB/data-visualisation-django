from django.urls import path
from . import views

app_name = 'csvs'
urlpatterns = [
    path('upload', views.upload_csv, name='upload')
]
