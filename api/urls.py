from django.urls import path
from . import views

urlpatterns = [
    path('getlistings/',views.getlistings,name='getlistings')
]