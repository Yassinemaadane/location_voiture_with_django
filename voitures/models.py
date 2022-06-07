from django.db import models

# Create your models here.

class Voiture(models.Model):
    Matricule = models.CharField(max_length=10 , primary_key=True)
    Image=models.ImageField(default='default.png',blank=True)
    Marque = models.CharField(max_length=50)
    Modele = models.CharField(max_length=50)
    TypePermis = models.CharField(max_length=1)
    parking=models.ForeignKey('parkings.Parking' ,null=True, on_delete=models.SET_NULL)
    offre=models.ForeignKey('offres.Offre' ,null=True, on_delete=models.SET_NULL)




# CREATE TABLE Voiture
# (
#      Matricule varchar(10) PRIMARY KEY ,
#  	 Marque varchar(50),
# 	 Modele varchar(50),
#      TypePermis char ,
#      IDpr varchar(10) ,
#      FOREIGN KEY (IDpr) REFERENCES Parking(Idp),
#      IDof varchar(10) ,
#      FOREIGN KEY (IDof) REFERENCES Offre(IdO)
# );