from django.conf.urls import url
from app import  views

app_name = "app"
urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    # url(r'^contact/$', views.contact, name="contact")
    # url(r'^getdata$', api_v1_views.get_all_venues_events),
    # url(r'^getvenue$', api_v1_views.get_venue),
    # url(r'^getevent$', api_v1_views.get_event),
    # url(r'^register$', api_v1_views.register),
    # url(r'^login$', api_v1_views.login),
    # url(r'^getmybookings$', api_v1_views.get_my_bookings)
]