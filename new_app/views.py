from django.shortcuts import render, redirect

from new_app.forms import food_form
from new_app.models import food


# Create your views here.
def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def kai(request):
    return render(request,'kai.html')

def food_add(request):
    form =food_form()
    if request.method == 'POST':
        data = food_form(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'food.html',{'form':form})


#VIEW
def food_view(request):
    data = food.objects.all()

    return render(request, 'view_data.html',{'data':data})


def food_delete(request,id):
    data = food.objects.get(id=id)
    data.delete()
    return redirect("viewfood")


def food_update(request,id):
    data = food.objects.get(id=id)
    form = food_form(instance = data)
    if request.method == 'POST':
        data = food_form(request.POST,instance=data)
        if data.is_valid():
           data.save()
           return redirect("viewfood")
    return render(request,'update.html',{'form':form})
