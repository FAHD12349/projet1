from django.urls import path, include
from .views import page_info
from page_assasiya.views import info_offre
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('about/', page_info, name='about'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

