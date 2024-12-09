from food.views import *
from django.urls import path
app_name='ola'

urlpatterns=[
    path('veg/',veg,name='veg'),
    path('nonveg/',nonveg,name='nonveg'),
]