from django.urls import path

from . import views


urlpatterns = [
    path('offre/', views.offre_list),
]
