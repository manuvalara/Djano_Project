from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index',views.index,name="index"),
    path('kai',views.kai,name='kai'),
    path('food',views.food_add,name="food")


]