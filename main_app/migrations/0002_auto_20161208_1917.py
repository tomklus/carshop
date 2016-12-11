# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel("Addresses", "Address"),
        migrations.RenameModel("Cars", "Car"),
        migrations.RenameModel("Repairs", "Repair"),
        migrations.RenameModel("Addresses", "Address"),
        migrations.RenameModel("Reservations", "Reservation"),
        migrations.RenameModel("TestDrives", "TestDrive"),
        migrations.RenameModel("Clients", "Client"),
        migrations.RenameModel("Employees", "Employee"),
        migrations.RenameModel("Invoices", "Invoice"),
        migrations.RenameModel("Orders", "Order"),
        migrations.RenameModel("Payments", "Payment"),
        migrations.RenameModel("RegistrationPlates", "RegistrationPlate"),

    ]
