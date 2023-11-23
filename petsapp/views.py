
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(req):
    data = HomeDB.objects.all()
    return render(req,'html/home.html', {'data':data})

def animals(req):
    andata = animalsDB.objects.all()
    return render(req,'html/animals.html', {'data':andata})

def cart(req, id):
    data = animalsDB.objects.get(pk=id)
    return render(req, 'html/cart.html', {'j':data})