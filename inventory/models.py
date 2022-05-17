from tkinter import CASCADE
from django.db import models

# Create your models here.

class Warehouse(models.Model):
    name = models.CharField('Warehouse name', max_length=100)
    address = models.CharField('Warehouse address', max_length=100)
    
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField('Item name', max_length=100)
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.name