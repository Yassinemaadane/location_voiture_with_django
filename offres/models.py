from django.db import models


class Offre(models.Model):
    IdOffre = models.CharField(max_length=50 , primary_key=True)
    DateDebut = models.DateField(null=True)
    DateDefin = models.DateField(null=True)
    solde = models.FloatField(null=True)
    def __str__(self):
        return self.IdOffre

# CREATE TABLE Offre
# (
#      IdO varchar(10) PRIMARY KEY ,
#  	 DateDebut Date,
# 	 DateFin Date,
#      Solde Float
# );