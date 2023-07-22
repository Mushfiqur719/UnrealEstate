from rest_framework.decorators import api_view
from rest_framework.response import Response
from listings.models import Listing
from .serializers import ListingSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_listings': '/',
    }
 
    return Response(api_urls)