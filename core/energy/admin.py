from django.contrib import admin
from .models import Building, Meter, Halfhourly

# Register your models here.
admin.site.register(Building)
admin.site.register(Meter)
admin.site.register(Halfhourly)
