from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('search/', views.search , name='search'),
    path('add-listing/',views.add_listing, name="add_listing"),
    path('edit-listing/<int:listing_id>/',views.edit_listing, name="edit_listing"),
    path('delete-listing/<int:listing_id>/',views.delete_listing, name="delete_listing"),
    path('add-realtor/',views.add_realtor, name="add_realtor"),
    path('edit-realtor/<int:realtor_id>/',views.edit_realtor, name="edit_realtor"),
]