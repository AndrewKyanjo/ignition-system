from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Hello, this is the HR index page.</h1>")

def say_hello(response):
    return HttpResponse("<h1>Hello from the HR app!</h1>")

def v1(response):
    return HttpResponse("<h1>Hello from the HR app v1!</h1>")