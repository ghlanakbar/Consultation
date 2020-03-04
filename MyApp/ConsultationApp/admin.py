from django.contrib import admin

# Register your models here.
from ConsultationApp.models import Consultation  #Configuiration du Table Consultation dans la base de donnée

admin.site.register(Consultation)
