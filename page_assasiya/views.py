from django.shortcuts import render
from .models import infoEcole, offre
from django.utils import timezone

def info_offre(request):
    ecoles = infoEcole.objects.all().prefetch_related('offre_set')
    offres = offre.objects.all()  
    current_year = timezone.now().year
    
    return render(request, "page_assasiya.html", { "ecoles": ecoles, "offres": offres, "current_year": current_year })


