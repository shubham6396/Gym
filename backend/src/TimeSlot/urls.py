from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'getAllTimeSlots', views.getAllTimeSlots),
    url(r'waitlist', views.addWaitlist),
]