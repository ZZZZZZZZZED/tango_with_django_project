from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

    
def index(request):
    return HttpResponse("Rango says hey there partner!")

