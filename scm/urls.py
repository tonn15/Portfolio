from django.urls import path
from . import views

app_name = 'scm'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('service', views.service, name = 'service'),
    path('contact-us', views.contact, name = 'contactus'),
]