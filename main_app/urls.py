"""carshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from main_app import views
from main_app.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^main_app/', views.dashboard),
    url(r'^search/', views.searchview, name='search_view'),
    url(r'^client/(?P<client_id>[0-9]+)', views.clientDetail, name='clientDetail'),
    url(r'^clients/', views.clientList,name='client_list'),
    url(r'^order/(?P<order_id>[0-9]+)', views.orderDetail, name='orderDetail'),
    url(r'^orders/', views.orderList,name='order_list'),
    url(r'^employee/(?P<employee_id>[0-9]+)', views.employeeDetail, name='employeeDetail'),
    url(r'^employees/$', views.employeeList, name='employee_list'),
    #url(r'^adds/$', AddressList.as_view(template_name="shop/client_list.html"),name='address_list'),
    url(r'^car/(?P<vin>([A-Z,a-z,0-9]+))', views.carDetail, name='carDetail'),
    url(r'^cars/$', views.carList, name='carList'),
    #url(r'^equipment/$', EquipmentList.as_view(template_name="shop/client_list.html"),name='equipment_list'),
    #url(r'^invoices/$', InvoiceList.as_view(template_name="shop/client_list.html"),name='invoice_list'),
    #url(r'^plates/$', PlatesList.as_view(template_name="shop/client_list.html"),name='plate_list'),
    #url(r'^repairs/$', RepairList.as_view(template_name="shop/client_list.html"),name='repair_list'),
    #url(r'^payments/$', PaymentList.as_view(template_name="shop/client_list.html"), name='payment_list'),
    #url(r'^reservations/$', ReservationList.as_view(template_name="shop/client_list.html"), name='reservation_list'),
    #url(r'^testdrives/$', TestDriveList.as_view(template_name="shop/client_list.html"), name='testdrive_list'),
    #url(r'^orders/$', OrderList.as_view(template_name="shop/client_list.html"), name='order_list'),
    url(r'^$', views.dashboard, name='dashboard'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.car_list, name='product_list_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.car_detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

