from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('search/', views.search , name='search'),
    path('add-listing/',views.add_listing, name="add_listing"),
    path('add-realtor/',views.add_realtor, name="add_realtor")
]