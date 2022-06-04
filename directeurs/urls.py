from django.urls import path

from . import views


urlpatterns = [
    path('dir/', views.directeurs_list),
]
