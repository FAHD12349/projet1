from django.urls import path
from .views import inscription, currentStudentView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('info/', views.currentStudentView.info, name='info'),
    
    # API endpoints for JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API endpoint for student data
    path('api/current-student/', currentStudentView.as_view(), name='current_student'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)