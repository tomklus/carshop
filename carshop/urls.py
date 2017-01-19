
from django.conf.urls import include, url
from django.contrib import admin
from main_app import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main_app.urls', namespace='main_app')),
]