from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> welcome to caleb\'s ')

def about(request):
    return HttpResponse('<h1> We are able to do any task </h1>')

def contact(request):
    return HttpResponse('<h1> my contact </h1>')
    
