"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from inventory import views

urlpatterns = [
    path('', views.all_inventory, name="home"),
    path('admin/', admin.site.urls),
    path('add/inventory', views.add_inventory, name='add-inventory'),
    path('add/warehouse', views.add_warehouse, name='add-warehouse'),
    path('edit/inventory/<item_id>', views.edit_inventory, name='edit-inventory'),
    path('delete/inventory/<item_id>',views.delete_inventory, name='delete-inventory'),
    path('delete/warehouse/<warehouse_id>',views.delete_warehouse, name='delete-warehouse')
]
