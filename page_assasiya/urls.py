from django.urls import path
from .views import info_offre, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('offre/',info_offre,name='offre'),   
    path('',home,name='home'),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)