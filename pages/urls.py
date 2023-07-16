from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('animal/', animal, name='animal'),
    path('animal/<pk>/', animal_detail, name='animal_detail'),
    path('business/', business, name='business'),
    path('business/<pk>/', business_detail, name='business_detail'),
    path('electro/', electro, name='electro'),
    path('electro/<pk>/', electro_detail, name='electro_detail'),
    path('furnature/', furnature, name='furnature'),
    path('furnature/<pk>/', furnature_detail, name='furnature_detail'),
    path('realty/', realty, name='realty'),
    path('transport/', transport, name='transport'),
    path('transport/<pk>/', transport_detail, name='transport_detail'),
]