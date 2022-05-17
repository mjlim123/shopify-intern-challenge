from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Warehouse
from .forms import ItemForm, WarehouseForm
from django.http import HttpResponseRedirect

def all_inventory(request):
    item_list = Item.objects.all()
    warehouse_list = Warehouse.objects.all()
    return render(request, 'home.html',{'item_list':item_list,
                                        'warehouse_list':warehouse_list})



def add_inventory(request):
    submitted = False
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add/inventory?submitted=True')
    else:
        form = ItemForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'add_inventory.html', {'form': form,
                                                  'submitted': submitted})
        
    
def add_warehouse(request):
    submitted = False
    if request.method == "POST":
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add/warehouse?submitted=True')
    else:
        form = WarehouseForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'add_warehouse.html', {'form': form,
                                                  'submitted': submitted})




def edit_inventory(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'edit-inventory.html', {'item':item,
                                                   'form':form})
    

def delete_inventory(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('home')


def delete_warehouse(request, warehouse_id):
    item = Warehouse.objects.get(pk=warehouse_id)
    item.delete()
    return redirect('home')




