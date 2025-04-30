from django.db import models

class Inscription(models.Model):
    nom=models.CharField(max_length=50)
    pernom=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    date_inscription=models.DateField()
    date_naissance=models.DateField()
    adresse=models.TextField()
    telephone=models.CharField(max_length=15)
    sexe=models.CharField(max_length=10)
    niveau=models.CharField(max_length=50)
    pays=models.CharField(max_length=50)
    ville=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return f"{self.nom}{self.pernom}{self.email}{self.age}{self.date_inscription}{self.date_naissance}{self.adresse}{self.telephone}{self.sexe}{self.niveau}{self.pays}{self.ville}{self.photo}"
    