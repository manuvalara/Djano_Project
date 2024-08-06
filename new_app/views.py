from django.shortcuts import render

from new_app.forms import food_form


# Create your views here.
def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def kai(request):
    return render(request,'kai.html')

def food_add(request):
    form =food_form()
    print(form)
    return render(request,'food.html',{'form':form})