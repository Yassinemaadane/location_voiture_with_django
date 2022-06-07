from django.urls import path
from django.urls import re_path


from . import views
app_name = 'voitures'


urlpatterns = [
    path('car/', views.car_list,name='car'),
    path('booking/', views.booking_list,name='booking'),
    path('car/<str:Matricule>/', views.car_detail,name='car_detail'),
]

 