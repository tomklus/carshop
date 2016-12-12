from django.http import HttpResponse
from .models import Addresses, Cars, Category
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):

    adds = Addresses.objects.all()
    name = 'Addresses'
    context = {'street' : 'Reymonta'}
    return render(request, 'index.html', {'addresses' : adds})

def car_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Cars.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
    return render(request,
                  'shop/car/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def car_detail(request, id, slug):
    product = get_object_or_404(Cars, id=id, slug=slug)
    return render(request, 'shop/car/detail.html', {'car': product})