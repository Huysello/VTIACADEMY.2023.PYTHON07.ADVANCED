from django.contrib import admin
from .models import Car, Manufacturer

admin.site.register(Manufacturer)
admin.site.register(Car)
