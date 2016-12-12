from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'number', 'city', 'zip', 'country', 'address_id', 'created', 'updated')
admin.site.register(Addresses, AddressAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'surname', 'shop', 'hire_date', 'gender', 'address', 'created', 'updated')
admin.site.register(Employees, EmployeeAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('vin', 'registration_plate', 'production_year', 'category', 'color', 'mileage', 'available', 'created', 'updated', 'slug', 'make')
    prepopulated_fields = {'slug': ('make',)}
admin.site.register(Cars, CarAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'surname', 'address', 'created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Clients, ClientAdmin)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('vin', 'number_of_airbags', 'power_steering', 'leather_seats', 'abs', 'esp', 'asr', 'automatic_gearbox', 'gps', 'aluminium_rims', 'created', 'updated')
admin.site.register(Equipment, EquipmentAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'order', 'client', 'invoice_status', 'created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('invoice_id',)}
admin.site.register(Invoices, InvoiceAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'vin', 'client', 'employee', 'invoice', 'created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('order_id',)}
admin.site.register(Orders, OrderAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'order', 'client', 'payment_method', 'amount', 'payment_date', 'created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('payment_id',)}
admin.site.register(Payments, PaymentAdmin)

class RegistrationPlateAdmin(admin.ModelAdmin):
    list_display = ('current_plate', 'previous_plates', 'vin', 'created', 'updated')
admin.site.register(RegistrationPlates, RegistrationPlateAdmin)

class RepairAdmin(admin.ModelAdmin):
    list_display = ('repair_id', 'typ', 'cost', 'description', 'vin', 'created', 'updated')
admin.site.register(Repairs, RepairAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'vin', 'from_date', 'until_date', 'client', 'created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('reservation_id',)}
admin.site.register(Reservations, ReservationAdmin)


class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('drive_id', 'client_id', 'drive_date', 'vin', 'created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('drive_id',)}
admin.site.register(TestDrives, TestDriveAdmin)