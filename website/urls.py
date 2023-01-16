from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [    
    path('acerca/', views.acerca, name='acerca'),
    path('mision_vision/', views.mision_vision, name='mision_vision'),
    path('servicios/', views.servicios, name='servicios'), 
    path('contacto/', views.contacto, name='contacto'), 
    path('panel/', views.panel, name='panel'),    
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
