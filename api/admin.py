from django.contrib import admin
from shoestore.models import Manufacturer, ShoeColor, ShoeType, Shoe
# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Shoe)
