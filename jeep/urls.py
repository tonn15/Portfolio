from django.urls import path
from . import views
app_name = 'jeep'
urlpatterns = [
    path('',views.index,name='index')
]