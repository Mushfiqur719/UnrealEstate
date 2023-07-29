from django import forms

from . models import Listing
from realtors.models import Realtor

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = "__all__"
