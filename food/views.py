from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def veg(request):
    return HttpResponse('<h1>Vegetarian<marquee> Idly,Sambar,Vada,Pongal</marquee></h1>')

def nonveg(request):
    return render(request,'nonveg.html')