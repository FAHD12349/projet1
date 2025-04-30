from rest_framework import serializers
from .models import Inscription

class InscriptionSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(max_length=50)
    pernom = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    date_inscription = serializers.DateField()
    date_naissance = serializers.DateField()
    adresse = serializers.CharField(max_length=500)    
    telephone = serializers.CharField(max_length=15)
    sexe = serializers.CharField(max_length=10)
    niveau = serializers.CharField(max_length=50)
    pays = serializers.CharField(max_length=50)
    ville = serializers.CharField(max_length=50)
    photo = serializers.ImageField()
    
    class Meta:
        model = Inscription
        fields = ['nom', 'pernom', 'email', 'age', 'date_inscription', 'date_naissance', 'adresse', 'telephone', 'sexe', 'niveau', 'pays', 'ville', 'photo']
