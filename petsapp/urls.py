
from django.urls import path 
from .import views
urlpatterns = [
     path('', views.home, name='home'), 
     path('animals', views.animals, name='animals'),
     path('cart/<int:id>', views.cart, name='cart'),
     path('cart', views.cart, name='cart'),

     
]
