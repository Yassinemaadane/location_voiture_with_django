from django.db import models

class Agence(models.Model):
    IdAgence = models.CharField(max_length=10 , primary_key=True)
    nom = models.CharField(max_length=50)
    emplacement = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    Tel = models.CharField(max_length=13)




# CREATE TABLE Agence
# (
#      IdA varchar(10) PRIMARY KEY ,
#  	 Nom varchar(50),
# 	 Emplacement varchar(150),
#   	 mail varchar(50),
#   	 Tel varchar(12)
# );
