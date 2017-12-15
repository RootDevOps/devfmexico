from django.conf.urls import url, include
from django.contrib import admin

from .views import login_view, logout_view, landing_page, registrer_view

urlpatterns = [
    url(r'^$', landing_page ,name = "home"),
    url(r'^login/', login_view ,name = "login"),
    url(r'^logout/', logout_view ,name = "logout"),
    url(r'^register/', registrer_view ,name = "register"),
]