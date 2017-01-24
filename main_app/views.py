from django.http import HttpResponse
from models import *
from django.shortcuts import render, get_object_or_404
import datetime
from django.views.generic import ListView
from django.core import serializers
from django.db import connection
from collections import namedtuple

# Create your views here.

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def searchview(request):

    query = request.POST.get('textfield', None)

    cursor = connection.cursor()
    cursor.execute('SELECT make, model, version, registration_plate, vin FROM cars '
                   'WHERE MATCH(make, model, color, version, registration_plate, vin)'
                   ' AGAINST(%s)', [query])
    rawcars = namedtuplefetchall(cursor)

    print rawcars
    for match in rawcars:
        result = {"Model": match.model, "Make": match.make, "Version": match.version, "Plate": match.registration_plate}
        print(match)

    cursor.execute('SELECT name, surname FROM clients '
                   'WHERE MATCH(name, surname)'
                   ' AGAINST(%s)', [query])
    rawclients = namedtuplefetchall(cursor)

    cursor.execute('SELECT name, surname FROM employees '
                   'WHERE MATCH(name, surname)'
                   ' AGAINST(%s)', [query])
    rawemployees = namedtuplefetchall(cursor)
    print (rawemployees)
    result = {}


    return render(request, 'shop/searchresults.html', {'cars': rawcars, 'clients': rawclients, 'employees': rawemployees})


def carDetail(request, vin):

    allCars = Cars.objects.all()
    car = allCars.filter(vin=vin)
    #carData = serializers.serialize("python", car)
    cursor = connection.cursor()


    # CAR
    cursor.execute('SELECT * FROM cars WHERE cars.vin = %s', [vin])
    cardata = namedtuplefetchall(cursor)

    if cardata:
        car = {"Make": cardata[0].make, "Model": cardata[0].model,"First registration": cardata[0].production_year,
               "Mileage": cardata[0].mileage,
               "Color": cardata[0].color, "Price [USD]": cardata[0].price, 
               "Version": cardata[0].version, "Registration plate": cardata[0].registration_plate}


    # REPAIRS
    cursor.execute('SELECT typ, description FROM repairs WHERE repairs.vin = %s', [vin])
    repairdata = namedtuplefetchall(cursor)

    if repairdata:
        repairs = {"Type": repairdata[0].typ, "Description": repairdata[0].description}
    else:
        repairs = {}

    # RESERVATIONS
    cursor.execute('SELECT client_id, from_date, until_date, reservation_id FROM reservations WHERE reservations.VIN = %s', [vin])
    reservationdata = namedtuplefetchall(cursor)



    if reservationdata:
        resClient_id = reservationdata[0].client_id
        resClient = Clients.objects.filter(client_id=resClient_id)
        reservation = {"Reservation ID": reservationdata[0].reservation_id, "Client": "%s %s" % (resClient[0].name, resClient[0].surname),
                       "From": reservationdata[0].from_date, "Until": reservationdata[0].until_date}
    else:
        reservation = {}

    # TEST DRIVES
    cursor.execute('SELECT drive_id, client_id, drive_date FROM test_drives WHERE test_drives.vin = %s', [vin])
    tdreiveData = namedtuplefetchall(cursor)


    if tdreiveData:
        tdriveclient_id = tdreiveData[0].client_id
        tdriveclient = Clients.objects.filter(client_id=tdriveclient_id)
        testdrive = {"Test drive ID": reservationdata[0].reservation_id,
                    "Client": "%s %s" % (tdriveclient[0].name, tdriveclient[0].surname),
                    "Drive date": tdreiveData[0].drive_date}
    else:
        testdrive = {}

    # EQUIPMENT
    cursor.execute('SELECT * FROM equipment WHERE equipment.VIN = %s', [vin])
    eqdata = namedtuplefetchall(cursor)


    if eqdata:

        equipment = {"Number of airbags": eqdata[0].number_of_airbags, "Power steering": eqdata[0].power_steering,
                     "Leather seats": eqdata[0].leather_seats, "ABS": eqdata[0].abs, "ESP": eqdata[0].esp,
                     "ASR": eqdata[0].asr, "Automatic gearbox": eqdata[0].automatic_gearbox, "GPS Radio": eqdata[0].gps,
                     "Aluminium Rims": eqdata[0].aluminium_rims}
    else:
        equipment = {}

    return render(request,'shop/car_detail.html', {'car': car, 'cars': allCars,
                                                   'equipment':equipment, 'testdrive': testdrive,
                                                   'reservation': reservation, 'repairs': repairs })

def carList(request):
    allcars = Cars.objects.all()

    cursor = connection.cursor()

    # FUNCTIONS
    cursor.execute('SELECT AVG(price) AS PriceAverage FROM cars')
    stats = namedtuplefetchall(cursor)

    cursor.execute('SELECT MAX(price) AS MaxPrice FROM cars')
    stats += namedtuplefetchall(cursor)

    cursor.execute('SELECT MIN(price) AS MinPrice FROM cars')
    stats += namedtuplefetchall(cursor)

    statistics = {"Average car price:": stats[0].PriceAverage,
             "Our most expensive car:": stats[1].MaxPrice,
             "Our cheapest car:": stats[2].MinPrice}
    print(statistics)
    return render(request, 'shop/base_car.html', {'cars': allcars, 'stats': statistics})


def dashboard(request):
    return render(request,'shop/dashboard.html',{'section': 'dashboard'})


def clientDetail(request, client_id):

    allClients = Clients.objects.all()
    cursor = connection.cursor()
    cursor.execute('SELECT clients.client_id, clients.name, clients.surname, addresses.street, '
                   'addresses.number, addresses.city, addresses.zip, addresses.country FROM '
                   'clients LEFT JOIN addresses ON clients.address_id=addresses.address_id '
                   'WHERE clients.client_id = %s', [client_id])
    clientData = namedtuplefetchall(cursor)

    if clientData:

        client = {"Client ID": clientData[0].client_id, "Name": clientData[0].name,
                     "Surname": clientData[0].surname}
    else:
        client = {}

    if clientData[0].street:
        address = {"Street": clientData[0].street, "Number": clientData[0].number,
                     "City": clientData[0].city, "ZIP Code": clientData[0].zip, "Country": clientData[0].country}
    else:
        address = {}

    return render(request,'shop/client_detail.html', {'client': client, 'clients': allClients, 'address':address})


def clientList(request):
    allClients = Clients.objects.all()
    return render(request, 'shop/base_clients.html', {'clients': allClients})

def orderDetail(request, order_id):
    order = Orders.objects.filter(order_id=order_id)
    allOrders = Orders.objects.all()

    cursor = connection.cursor()
    cursor.execute('SELECT orders.VIN, orders.client_id, orders.employee_id, invoices.invoice_status, '
                   'invoices.invoice_id FROM orders LEFT JOIN invoices ON orders.order_id=invoices.order_id '
                   'WHERE orders.order_id = %s', [order_id])
    orderdata = namedtuplefetchall(cursor)

    if orderdata:
        order = {"Client": "%s" % order[0].client,
                 "Employee": "%s" % order[0].employee,
                     "Car VIN": orderdata[0].VIN}
    else:
        order = {}

    if orderdata[0].invoice_id:
        invoice = {"Status": orderdata[0].invoice_status, "Invoice ID": orderdata[0].invoice_id}
    else:
        inovice = {}

    cursor.execute('SELECT payments.payment_method, payments.amount, '
                   'payments.payment_date FROM payments WHERE order_id = %s', [order_id])
    paymentdata = namedtuplefetchall(cursor)

    if paymentdata:
        payment = {"Method": paymentdata[0].payment_method, "Amount": paymentdata[0].amount,
                   "Paymnent date": paymentdata[0].payment_date}
    else:
        payment = {}

    print(order)
    print(invoice)
    print(payment)

    return render(request, 'shop/order_detail.html', {'order': order, 'orders': allOrders,
                                                      'invoice': invoice, 'payment': payment})


def orderList(request):
    allOrders = Orders.objects.all()
    return render(request, 'shop/base_orders.html', {'orders': allOrders})


def employeeList(request):
    allemployees = Employees.objects.all()
    return render(request, 'shop/base_employees.html', {'employees': allemployees})

def employeeDetail(request, employee_id):

    allemployees = Employees.objects.all()
    cursor = connection.cursor()
    cursor.execute('SELECT employees.employee_id, employees.name, employees.surname, employees.gender,'
                   ' employees.hire_date, addresses.street, '
                   'addresses.number, addresses.city, addresses.zip, addresses.country FROM '
                   'employees LEFT JOIN addresses ON employees.address_id=addresses.address_id '
                   'WHERE employees.employee_id = %s', [employee_id])
    employeedata = namedtuplefetchall(cursor)

    if employeedata:

        employee = {"Employee ID": employeedata[0].employee_id, "Name": employeedata[0].name,
                    "Surname": employeedata[0].surname, "Gender": employeedata[0].gender,
                    "Hire Date": employeedata[0].hire_date}
    else:
        employee = {}

    if employeedata[0].street:
        address = {"Street": employeedata[0].street, "Number": employeedata[0].number,
                     "City": employeedata[0].city, "ZIP Code": employeedata[0].zip, "Country": employeedata[0].country}
    else:
        address = {}

    return render(request,'shop/employee_detail.html', {'employee': employee, 'employees': allemployees, 'address': address})




