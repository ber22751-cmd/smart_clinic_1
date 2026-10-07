
from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES = (
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
    ('admin', 'Admin'),
)

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=USER_ROLES)

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    license_expiry = models.DateField(null=True, blank=True)  
    available_times = models.TextField(blank=True)            
    clinic = models.ForeignKey(Clinic, null=True, blank=True, on_delete=models.CASCADE)

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.user.username} with Dr. {self.doctor.user.username} on {self.date} at {self.time}"
