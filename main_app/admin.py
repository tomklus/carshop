from django.contrib import admin

# Register your models here.
from .models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'number', 'city', 'zip', 'country', 'address_id')
admin.site.register(Addresses, AddressAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'surname', 'shop', 'hire_date', 'gender', 'address')
admin.site.register(Employees, EmployeeAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('vin', 'registration_plate', 'production_year', 'category', 'color', 'milage', 'status')
admin.site.register(Cars, CarAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'surname', 'address')
admin.site.register(Clients, ClientAdmin)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('vin', 'number_of_airbags', 'power_steering', 'leather_seats', 'abs', 'esp', 'asr', 'automatic_gearbox', 'gps', 'aluminium_rims')
admin.site.register(Equipment, EquipmentAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'order', 'client', 'invoice_status', 'created', 'modified')
admin.site.register(Invoices, InvoiceAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'vin', 'client', 'employee', 'invoice', 'created', 'modified')
admin.site.register(Orders, OrderAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order', 'client', 'payment_method', 'amount', 'payment_date')
admin.site.register(Payments, PaymentAdmin)

class RegistrationPlateAdmin(admin.ModelAdmin):
    list_display = ('current_plate', 'previous_plates', 'vin')
admin.site.register(RegistrationPlates, RegistrationPlateAdmin)

class RepairAdmin(admin.ModelAdmin):
    list_display = ('repair_id', 'typ', 'cost', 'description', 'vin')
admin.site.register(Repairs, RepairAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'vin', 'from_date', 'until_date', 'client', 'created', 'modified')
admin.site.register(Reservations, ReservationAdmin)


class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('drive_id', 'client', 'drive_date', 'vin', 'created', 'modified')
admin.site.register(TestDrives, TestDriveAdmin)