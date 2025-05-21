from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Inscription
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .Serializer import InscriptionSerializer

@login_required
def inscription(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        CNIE = request.POST.get('CNIE')
        if Inscription.objects.filter(CNIE=CNIE).exists():
            return render(request, 'page.html', {'error_message': 'Un compte avec cet CNIE existe déjà!'})
        
        utilisateur = Inscription(
            nom=request.POST.get('nom'),
            pernom=request.POST.get('prenom'),
            email=request.user.email,  # Use authenticated user's email
            age=request.POST.get('age'),
            CNIE=CNIE,
            specialites=request.POST.get('specialites'),
            date_inscription=request.POST.get('date_inscription'),
            date_naissance=request.POST.get('date_naissance'),
            adresse=request.POST.get('adresse'),
            telephone=request.POST.get('telephone'),
            sexe=request.POST.get('sexe'),
            niveau=request.POST.get('niveau'),
            pays=request.POST.get('pays'),
            ville=request.POST.get('ville'),
            photo=request.FILES.get('photo')
        )
        utilisateur.save()
        return render(request, 'home.html', {'message': 'Inscription réussie !'})
    
    return render(request, 'page.html')

class currentStudentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            student=Inscription.objects.filter(email=request.user.email)
            serializer=InscriptionSerializer(student,many=True)
            return Response(serializer.data)
        except Inscription.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)
        


    def info(request):
        return render(request,'info.html')
