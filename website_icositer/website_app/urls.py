from django.conf.urls import url, include
from django.urls import path
from website_app.views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('about', about, name='about'),
    path('competition', competition, name='competition'),
]