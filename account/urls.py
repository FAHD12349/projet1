
from django.urls import path, include
from . import views
from .views import register, user_login, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/login/', views.auth_login, name='api_login'),
    path('', include('pages.urls')),

   
 
]

