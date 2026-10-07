from django.contrib import admin
from .models import User, PatientProfile, DoctorProfile, Clinic, Appointment

admin.site.register(User)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(Clinic)
admin.site.register(Appointment)
