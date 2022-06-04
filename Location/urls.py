from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.Index),
    path('admin/', admin.site.urls),
    path('dirs/', include('directeurs.urls')),
    path('offres/', include('offres.urls')),
    ]
