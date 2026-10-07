from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, PatientProfile, DoctorProfile, Appointment

class PatientSignUpForm(UserCreationForm):
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label="Gender")
    medical_history = forms.CharField(widget=forms.Textarea, label="Medical History", required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'gender', 'medical_history']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'patient'
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                gender=self.cleaned_data['gender'],
                medical_history=self.cleaned_data['medical_history']
            )
        return user


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['specialization', 'license_number', 'license_expiry', 'available_times', 'clinic']
        widgets = {
            'license_expiry': forms.DateInput(attrs={'type': 'date'}),
            'available_times': forms.Textarea(attrs={'rows': 4}),
        }




class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(role='doctor'), label="اختر دكتور")
    
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
        }
