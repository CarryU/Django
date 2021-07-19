from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
      return HttpResponse("Hello Django!")

def new_index(request):
     return  render(request,'news/first.html')