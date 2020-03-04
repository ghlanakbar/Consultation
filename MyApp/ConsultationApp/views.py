#les views 

# django utlise le modele , view et templates
from django.shortcuts import render

# Create your views here.

from ConsultationApp import models
from ConsultationApp import forms



def Consultation(request): #view du liste des Consultations
	consultations=models.Consultation.objects.all()
	context={
	'consultations':consultations
	}
	return render(request,'consultations.html',context)

def Register(request): #view du formulaire Consultation
	form_data=forms.ConsultationRegistrer(request.POST or None)
	msg=''
	if form_data.is_valid():
		consultation=models.Consultation()
		consultation.nom=form_data.cleaned_data['nom']
		consultation.prenom=form_data.cleaned_data['prenom']
		consultation.date_naissance=form_data.cleaned_data['date_naissance']
		#consultation.photo=form_data.cleaned_data['photo']
		consultation.sexe=form_data.cleaned_data['sexe']
		consultation.groupe_sanguin=form_data.cleaned_data['groupe_sanguin']
		consultation.poids=form_data.cleaned_data['poids']
		consultation.taille=form_data.cleaned_data['taille']
		consultation.observations=form_data.cleaned_data['observations']
		consultation.save()
		msg='Enregister avec succer'

	context={
		'formregister':form_data,
		'msg':msg
		}
	return render(request,'register.html',context)
