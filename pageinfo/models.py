from django.db import models

class PageInfo(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    presontation_generale = models.TextField()
    loi = models.TextField()
    vedio =models.FileField(upload_to='vedios/', blank=True, null=True)
    Historique = models.TextField()
    Partenaires = models.TextField()
    url=models.URLField()
   