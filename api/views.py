from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from listings.models import Listing
from .serializers import ListingSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_listings': '/',
    }
    return Response(api_urls)


@api_view(['GET'])
def getlistings(request):
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings,many=True)
    return JsonResponse(serializer.data, safe = False)