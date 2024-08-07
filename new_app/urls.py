from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index',views.index,name="index"),
    path('kai',views.kai,name='kai'),
    path('food',views.food_add,name="food"),
    path("viewfood",views.food_view,name="viewfood"),
    path('food_delete/<int:id>/',views.food_delete,name= 'food_delete'),
    path('food_update/<int:id>/',views.food_update,name= 'food_update')


]