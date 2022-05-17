from django.contrib import admin
from .models import Warehouse
from .models import Item


# Register your models here.

admin.site.register(Warehouse)
admin.site.register(Item)