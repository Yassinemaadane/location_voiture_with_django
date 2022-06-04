from django.db import models

# Create your models here.

class Parking(models.Model):
    Idparking = models.CharField(max_length=10 , primary_key=True)
    nom = models.CharField(max_length=50)
    Emplacement = models.CharField(max_length=50)
    agence=models.ForeignKey('agences.Agence' ,null=True, on_delete=models.SET_NULL)


# CREATE TABLE Parking
# (
#      Idp varchar(10) PRIMARY KEY ,
#  	 Nom varchar(50),
# 	 Emplacement varchar(50),
#      idAG varchar(10) ,
#      FOREIGN KEY (idAG) REFERENCES Agence(IdA)
# );