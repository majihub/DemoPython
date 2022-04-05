import requests
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    QUERY=None
    PRODUCTS=None
    if 'q' in request.GET:
        QUERY=request.GET.get('q')
        PRODUCTS=Product.objects.all().filter(Q(name__contains=QUERY) | Q(description__contains=QUERY))
    return render(request,"search.html",{'query':QUERY,'products':PRODUCTS})