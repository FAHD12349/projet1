from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
   
    path('admin/', admin.site.urls, name='admin'),
    path('', include('pages.urls')),
    path('', include('page_assasiya.urls')),
    path('', include('pageinfo.urls')),
    path('', include('account.urls')),
    path('token',TokenObtainPairView.as_view()),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)