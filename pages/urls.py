from django.urls import path
from .views import inscription, currentStudentView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
     path('inscription/', inscription, name='inscription'),
    path('info/', currentStudentView.as_view(), name='info'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)