from django.db import models

class Piva(models.Model):
    Nomi=models.CharField(max_length=200)
    Narxi=models.IntegerField()
    Rasmi=models.ImageField(upload_to='Pivo')
    Tarif=models.TextField()
    def __str__(self):
        return self.Nomi
class Taom(models.Model):
    Nomi=models.CharField(max_length=200)
    Narxi=models.IntegerField()
    Rasmi=models.ImageField(upload_to='taom')
    Tarif=models.TextField()
    def __str__(self):
        return self.Nomi
class Salat(models.Model):
    Nomi=models.CharField(max_length=200)
    Narxi=models.IntegerField()
    Rasmi=models.ImageField(upload_to='Salat')
    Tarif=models.TextField()
    def __str__(self):
        return self.Nomi