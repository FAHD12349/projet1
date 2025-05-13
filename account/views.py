from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import signupSerializer
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# تسجيل المستخدم
def register(request):
    if request.method == 'POST':
        data = request.POST
        user_serializer = signupSerializer(data=data)

        if user_serializer.is_valid():
            if not User.objects.filter(email=data['email']).exists():
                user = User.objects.create(
                    username=data['username'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    password=make_password(data['password'])
                )
                return redirect('login')  
            else:
                return HttpResponse("email no valide ", status=400) 
        else:
            return HttpResponse("problem de validation", status=400)  
    return render(request, 'account.html')



@csrf_exempt  
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

           
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

           
            return JsonResponse({
                'status': 'success',
                'message': 'Login successful',
                'access_token': access_token, 
                'refresh_token': str(refresh)
            })

        else:
            return JsonResponse({'status': 'error', 'message': 'les données sont incorrectes'}, status=400)  
    
    return render(request, 'login.html')



def user_logout(request):
    auth_logout(request)
    return redirect('home') 