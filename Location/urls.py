from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Index),
    path('admin/', admin.site.urls),
    path('dirs/', include('directeurs.urls')),
    path('offres/', include('offres.urls')),
    path('cars/', include('voitures.urls')),
    ]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)