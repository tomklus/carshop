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
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models



class Addresses(models.Model):
    street = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    address_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street + " " + self.number

    def __unicode__(self):
        return u'%s %s' %(self.street ,self.number)

    class Meta:
        managed = True

        db_table = 'addresses'


class Cars(models.Model):
    vin = models.CharField(db_column='VIN', primary_key=True, max_length=17)  # Field name made lowercase.
    registration_plate = models.ForeignKey('RegistrationPlates', db_column='registration_plate', blank=True, null=True)
    production_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)
    price = models.IntegerField(blank=True, null=True)
    make = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s %s %s %s' %(self.vin, self.make, self.model, self.production_year)

    def __str__(self):
        return str(self.vin)


    class Meta:
        ordering = ('make',)
        managed = True
        db_table = 'cars'


class Clients(models.Model):
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey(Addresses, blank=True, null=True)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' %(self.name ,self.surname)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        managed = True
        db_table = 'clients'


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    shop = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.ForeignKey(Addresses, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' %(self.name ,self.surname)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        managed = True
        db_table = 'employees'


class Equipment(models.Model):
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    eq_id = models.IntegerField(primary_key=True)
    number_of_airbags = models.IntegerField(blank=True, null=True)
    power_steering = models.IntegerField(blank=True, null=True)
    leather_seats = models.IntegerField(blank=True, null=True)
    abs = models.IntegerField(blank=True, null=True)
    esp = models.IntegerField(blank=True, null=True)
    asr = models.IntegerField(blank=True, null=True)
    automatic_gearbox = models.IntegerField(blank=True, null=True)
    gps = models.IntegerField(blank=True, null=True)
    aluminium_rims = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' %(self.eq_id, self.vin)

    def __str__(self):
        return str(self.eq_id)

    class Meta:
        db_table = 'equipment'


class Invoices(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('Orders', blank=True, null=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    invoice_status = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s %s' %(self.invoice_id ,self.order)

    def __str__(self):
        return str(self.invoice_id)

    class Meta:
        managed = True
        db_table = 'invoices'


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    client = models.ForeignKey(Clients, blank=True, null=True)
    employee = models.ForeignKey(Employees, blank=True, null=True)
    invoice = models.ForeignKey(Invoices, blank=True, null=True)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s %s %s' %(self.order_id, self.client, self.vin)

    def __str__(self):
        return str(self.order_id)

    class Meta:
        managed = True
        db_table = 'orders'


class Payments(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Orders, blank=True, null=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    payment_method = models.CharField(max_length=8, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' %(self.payment_id, self.order)

    def __str__(self):
        return str(self.payment_id)

    class Meta:
        managed = True
        db_table = 'payments'


class RegistrationPlates(models.Model):
    current_plate = models.CharField(primary_key=True, max_length=10)
    previous_plates = models.CharField(max_length=50, blank=True, null=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s' %(self.current_plate)

    def __str__(self):
        return self.current_plate

    class Meta:
        managed = True
        db_table = 'registration_plates'


class Repairs(models.Model):
    repair_id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=30, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s ' %(self.repair_id, self.vin)

    def __str__(self):
        return str(self.repair_id)

    class Meta:
        managed = True
        db_table = 'repairs'


class Reservations(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    from_date = models.DateField(blank=True, null=True)
    until_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' %(self.reservation_id, self.client)

    def __str__(self):
        return str(self.reservation_id)

    class Meta:
        managed = True
        db_table = 'reservations'


class TestDrives(models.Model):
    drive_id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Clients, blank=True, null=True)
    drive_date = models.DateTimeField(blank=True, null=True)
    vin = models.ForeignKey(Cars, db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s %s %s' %(self.vin, self.client, self.drive_date)

    def __str__(self):
        return str(self.drive_id)

    class Meta:
        managed = True
        db_table = 'test_drives'


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
