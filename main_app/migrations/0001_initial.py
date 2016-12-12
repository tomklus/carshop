# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('street', models.CharField(max_length=20, null=True, blank=True)),
                ('number', models.CharField(max_length=10, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('zip', models.CharField(max_length=10, null=True, blank=True)),
                ('country', models.CharField(max_length=20, null=True, blank=True)),
                ('address_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'addresses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('vin', models.CharField(max_length=17, serialize=False, primary_key=True, db_column='VIN')),
                ('production_year', models.TextField(null=True, blank=True)),
                ('category', models.CharField(max_length=20, null=True, blank=True)),
                ('color', models.CharField(max_length=20, null=True, blank=True)),
                ('mileage', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'cars',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('surname', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'clients',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('surname', models.CharField(max_length=20, null=True, blank=True)),
                ('shop', models.CharField(max_length=20, null=True, blank=True)),
                ('hire_date', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('vin', models.CharField(max_length=17, serialize=False, primary_key=True, db_column='VIN')),
                ('number_of_airbags', models.IntegerField(null=True, blank=True)),
                ('power_steering', models.IntegerField(null=True, blank=True)),
                ('leather_seats', models.IntegerField(null=True, blank=True)),
                ('abs', models.IntegerField(null=True, blank=True)),
                ('esp', models.IntegerField(null=True, blank=True)),
                ('asr', models.IntegerField(null=True, blank=True)),
                ('automatic_gearbox', models.IntegerField(null=True, blank=True)),
                ('gps', models.IntegerField(null=True, blank=True)),
                ('aluminium_rims', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'equipment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoice_id', models.IntegerField(serialize=False, primary_key=True)),
                ('invoice_status', models.CharField(max_length=20, null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'invoices',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(serialize=False, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.IntegerField(serialize=False, primary_key=True)),
                ('payment_method', models.CharField(max_length=8, null=True, blank=True)),
                ('amount', models.FloatField(null=True, blank=True)),
                ('payment_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'payments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RegistrationPlates',
            fields=[
                ('current_plate', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('previous_plates', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'registration_plates',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Repairs',
            fields=[
                ('repair_id', models.IntegerField(serialize=False, primary_key=True)),
                ('typ', models.CharField(max_length=30, null=True, blank=True)),
                ('cost', models.FloatField(null=True, blank=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'repairs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('reservation_id', models.IntegerField(serialize=False, primary_key=True)),
                ('from_date', models.DateField(null=True, blank=True)),
                ('until_date', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'reservations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestDrives',
            fields=[
                ('drive_id', models.IntegerField(serialize=False, primary_key=True)),
                ('customer_id', models.IntegerField(null=True, blank=True)),
                ('drive_date', models.DateTimeField(null=True, blank=True)),
                ('vin', models.CharField(max_length=17, null=True, db_column='VIN', blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test_drives',
                'managed': True,
            },
        ),
    ]
