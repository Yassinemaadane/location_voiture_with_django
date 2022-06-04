from django.db import models

# Create your models here.
class Chauffeur(models.Model):
    cinC = models.CharField(max_length=50 , primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    Tel = models.CharField(max_length=13)
    TypePermis = models.CharField(max_length=50, null=False)
    Diplome = models.CharField(max_length=50)
    agence=models.ForeignKey('agences.Agence' ,null=True, on_delete=models.SET_NULL)




# CREATE TABLE Chauffeur
# (
#      Cin varchar(10) PRIMARY KEY ,
#  	 Nom varchar(50),
# 	 Prenom varchar(50),
#   	 Adresse varchar(50),
#   	 Tel varchar(12),
#  	 Email varchar(50),
# 	 Pass varchar(50),
#      TypePermis char NOT Null,
#      idAG varchar(10) ,
#      FOREIGN KEY (idAG) REFERENCES Agence(IdA)
# );