from django.http import HttpResponse
from .models import Addresses
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):

    adds = Addresses.objects.all()
    name = 'Addresses'
    context = {'street' : 'Reymonta'}
    return render(request, 'index.html', {'addresses' : adds})