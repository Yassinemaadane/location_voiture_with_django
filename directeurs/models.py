from django.db import models

class Directeur(models.Model):
    Cin = models.CharField(max_length=50 , primary_key=True)
    Pass = models.CharField(max_length=55 )