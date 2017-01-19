from django.http import HttpResponse
from models import *
from django.shortcuts import render, get_object_or_404
import datetime
from django.views.generic import ListView

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def dashboard(request):
    return render(request,'shop/dashboard.html',{'section': 'dashboard'})

class DetailList(ListView):
    model = [Clients, Cars]


class ClientList(ListView):
    model = Clients

class AddressList(ListView):
    model = Addresses

class CarList(ListView):
    model = Cars

class EmployeeList(ListView):
    model = Employees

class EquipmentList(ListView):
    model = Equipment

class InvoiceList(ListView):
    model = Invoices

class OrderList(ListView):
    model = Orders

class PaymentList(ListView):
    model = Payments

class PlatesList(ListView):
    model = RegistrationPlates

class RepairList(ListView):
    model = Repairs

class ReservationList(ListView):
    model = Reservations

class TestDriveList(ListView):
    model = TestDrives


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