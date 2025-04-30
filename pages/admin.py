from django.contrib import admin
from .models import Inscription


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'pernom', 'email', 'age', 'date_inscription', 'date_naissance', 'adresse', 'telephone', 'sexe', 'niveau', 'pays', 'ville', 'photo')
    search_fields = ('nom', 'pernom', 'email')
    list_filter = ( 'niveau', 'pays', 'ville')
    
    
admin.site.register(Inscription, InscriptionAdmin)
admin.site.site_header = "Administration"
admin.site.site_title = "Administration"