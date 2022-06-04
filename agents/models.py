from django.db import models

# Create your models here.

# from .agences.models import Agence 
class Agent(models.Model):
    cinA = models.CharField(max_length=50 , primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    Tel = models.CharField(max_length=13)
    Pass = models.CharField(max_length=50)
    Diplome = models.CharField(max_length=50)
    agence=models.ForeignKey('agences.Agence' ,null=True, on_delete=models.SET_NULL)





# CREATE TABLE Agent
# (
#      Cin varchar(10) PRIMARY KEY ,
#  	 Nom varchar(50),
# 	 Prenom varchar(50),
#   	 Adresse varchar(50),
#   	 Tel varchar(12),
#  	 Email varchar(50),
# 	 Pass varchar(50),
#      Diplome varchar(50) NOT Null,
#      idAG varchar(10) ,
#      FOREIGN KEY (idAG) REFERENCES Agence(IdA)
# );
