



#formular
from django import forms
from .models import Consultation

s_choice = (
		('femme', 'Femme'),
		('homme', 'Homme'),   #type du sexe
		)
g_choice = (
		('o+', 'O+'),
		('o-', 'O-'),
		('b+', 'B+'),
		('b-', 'B-'),  #type de groupe sangui
		('a-', 'A-'),
		('a+', 'A+'),
		('ab-','AB-'),
		('ab+','AB+'),	
		)
t_choice = (
		('aaaa-mm-jj', 'aaaa-mm-jj'),
		)

class ConsultationRegistrer(forms.Form):
	#photo = forms.ImageField(required=True)
	nom = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
	prenom = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
	date_naissance = forms.CharField(required=True, widget=forms.DateInput(attrs={'class': 'form-control'} ))
	fomat= forms.ChoiceField(choices=t_choice)
	sexe = forms.ChoiceField(choices=s_choice) 
	groupe_sanguin = forms.ChoiceField(choices=g_choice)
	poids = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
	taille = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
	observations = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'} ))