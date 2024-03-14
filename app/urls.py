from django.urls import path 
from .views import add , get , get_all , delete , updete , get_name ,lst_models , get_color , get_madel , get_in , get_price

urlpatterns = [
    path('add/' , add),
    path('get/<int:pk>/' , get ),
    path('get/all/' , get_all ),
    path('delete/<int:pk>/' , delete ),
    path('updete/' , updete ),
    path('name/<name>/' , get_name),
    path('model/' , lst_models),
    path('color/<color>/' , get_color),
    path('model/<model>/' , get_madel),
    path('in/<int:price1>/<int:price2>/' , get_in),
    path('price/<int:prike>/' , get_price),

]