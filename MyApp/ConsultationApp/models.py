


#les modeles 
from django.db import models

# Create your models here.

class Consultation(models.Model):
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	date_naissance= models.DateTimeField()
	
	photo = models.ImageField(upload_to='images/', blank=True)
	s_choice = (
		('femme', 'Femme'), #type du sexe
		('homme', 'Homme'),
		)
	g_choice = (
		('o-', 'O-'), #type de groupe sangui
		('o+', 'O+'),
		('b+', 'B+'),
		('b-', 'B-'),
		('a-', 'A-'),
		('a+', 'A+'),
		('ab-', 'AB-'),
		('ab+','AB+'),	
		)
	sexe = models.CharField(max_length=200, choices=s_choice)
	groupe_sanguin=models.CharField(max_length=200, choices=g_choice)
	poids = models.FloatField(default=0.0)  #poids
	taille = models.FloatField(default=0.0)  #Taille
	observations = models.CharField(max_length=2000)
	def __str__(self): #metode qui retoure nom de l'objet
		return self.nom