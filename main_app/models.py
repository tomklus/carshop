# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Addresses(models.Model):
    street = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    address_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.street + " " + self.number

    class Meta:
        managed = False
        db_table = 'addresses'


class Cars(models.Model):
    vin = models.CharField(db_column='VIN', primary_key=True, max_length=17)  # Field name made lowercase.
    registration_plate = models.ForeignKey('RegistrationPlates', db_column='registration_plate', blank=True, null=True)
    production_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    milage = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.vin


    class Meta:
        managed = False
        db_table = 'cars'


class Clients(models.Model):
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey(Addresses, blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        managed = False
        db_table = 'clients'


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    shop = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.ForeignKey(Addresses, blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        managed = False
        db_table = 'employees'


class Equipment(models.Model):
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    number_of_airbags = models.IntegerField(blank=True, null=True)
    power_steering = models.IntegerField(blank=True, null=True)
    leather_seats = models.IntegerField(blank=True, null=True)
    abs = models.IntegerField(blank=True, null=True)
    esp = models.IntegerField(blank=True, null=True)
    asr = models.IntegerField(blank=True, null=True)
    automatic_gearbox = models.IntegerField(blank=True, null=True)
    gps = models.IntegerField(blank=True, null=True)
    aluminium_rims = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.vin

    class Meta:
        managed = False
        db_table = 'equipment'


class Invoices(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('Orders', blank=True, null=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    invoice_status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.invoice_id

    class Meta:
        managed = False
        db_table = 'invoices'


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    client = models.ForeignKey(Clients, blank=True, null=True)
    employee = models.ForeignKey(Employees, blank=True, null=True)
    invoice = models.ForeignKey(Invoices, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.order_id

    class Meta:
        managed = False
        db_table = 'orders'


class Payments(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Orders, blank=True, null=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    payment_method = models.CharField(max_length=8, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.payment_id

    class Meta:
        managed = False
        db_table = 'payments'


class RegistrationPlates(models.Model):
    current_plate = models.CharField(primary_key=True, max_length=10)
    previous_plates = models.CharField(max_length=50, blank=True, null=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.current_plate

    class Meta:
        managed = False
        db_table = 'registration_plates'


class Repairs(models.Model):
    repair_id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=30, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.repair_id

    class Meta:
        managed = False
        db_table = 'repairs'


class Reservations(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    from_date = models.DateField(blank=True, null=True)
    until_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.reservation_id

    class Meta:
        managed = False
        db_table = 'reservations'


class TestDrives(models.Model):
    drive_id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    drive_date = models.DateTimeField(blank=True, null=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.drive_id

    class Meta:
        managed = False
        db_table = 'test_drives'
