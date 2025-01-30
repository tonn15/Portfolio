from django.urls import path
from . import views
app_name = 'cuteness-overload'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('details', views.details, name = 'details')
]
