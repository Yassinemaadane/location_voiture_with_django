from django.db import models

# Create your models here.

class Client(models.Model):
    cinCl = models.CharField(max_length=50 , primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    Tel = models.CharField(max_length=13)
    TypePermis = models.CharField(max_length=1, null=False)
    fidelite = models.BooleanField(default=False)
    

# CREATE TABLE Client
# (
#      Cin varchar(10) PRIMARY KEY ,
#  	 Nom varchar(50),
# 	 Prenom varchar(50),
#   	 Adresse varchar(50),
#   	 Tel varchar(12),
#  	 Email varchar(50),
# 	 Pass varchar(50),
#      TypePermis char,
#      fidelite boolean
# );