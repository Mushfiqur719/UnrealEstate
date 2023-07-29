from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import ListingForm, RealtorForm
from django.core.paginator import Paginator
from .choices import bedroom_choices,area_choices, price_choices, size_choices

def index(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    context = {'listings':listings}
    return render(request, 'listings/listings.html',context)

def add_listing(request):
    form = ListingForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("listings")
    else:
        form = ListingForm()
    return render(request,"listings/add_listing.html", {'form':form})

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing' : listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-listing_date')
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) 

    if 'city' in request.GET:
        city = request.GET['city'] 
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)  

    if 'area' in request.GET:
        area = request.GET['area'] 
        if area:
            queryset_list = queryset_list.filter(state__iexact=area)    
    
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms'] 
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)   

    if 'price' in request.GET:
        price = request.GET['price'] 
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    if 'size' in request.GET:
        size = request.GET['size'] 
        if size:
            queryset_list = queryset_list.filter(size__lte=size)       
                                    
    context = {
        'bedroom_choices': bedroom_choices,
        'area_choices': area_choices,
        'price_choices': price_choices,
        'size_choices': size_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)    