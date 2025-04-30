from django.shortcuts import render
from django.http import HttpResponse
from .models import PageInfo
from django.utils import timezone
from page_assasiya.models import  infoEcole

def page_info(request):
    page_info = PageInfo.objects.first()
    ecles = infoEcole.objects.all()
    current_year = timezone.now().year
    return render(request, 'page_info.html', {'page_info': page_info, 'ecoles': ecles})
