from django.db import models


class infoEcole(models.Model):
    nom=models.CharField(max_length=50)
    adresse=models.TextField()
    telephone=models.CharField(max_length=15)
    email=models.EmailField()
    cover_image = models.ImageField(upload_to='photos/', blank=True, null=True)
    
def __str__(self):
    return f"{self.nom}, {self.adresse}, {self.telephone} ,{self.email}"


class offre(models.Model):
    school=models.ForeignKey(infoEcole, on_delete=models.CASCADE)
    spesialiter=models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.school}, {self.spesialiter}, {self.duration}, {self.price}"
    


