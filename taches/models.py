from django.db import models

# Create your models here.
class Tache(models.Model):
    IdTache = models.CharField(max_length=10 , primary_key=True)
    DateDebut = models.DateField()
    DateFin = models.DateField()
    agence=models.ForeignKey('voitures.Voiture' ,null=True, on_delete=models.SET_NULL)
    chauffeur= models.ForeignKey('chauffeurs.Chauffeur' ,null=True, on_delete=models.SET_NULL)


# CREATE TABLE Tache
# (
#      IdT varchar(10) PRIMARY KEY ,
#  	 DateDebut Date,
# 	 DateFin Date,
#      Mt varchar(10) ,
#      FOREIGN KEY (Mt) REFERENCES Voiture(Matricule),
#      Ch varchar(10) ,
#      FOREIGN KEY (Ch) REFERENCES Chauffeur(Cin)
# );