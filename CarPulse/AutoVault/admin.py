from django.contrib import admin
from .models import Car, CarDocument, CarExpense, CarImage, Make, Model

# Register your models here.
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(CarDocument)
admin.site.register(CarExpense)