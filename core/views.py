from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, DoctorProfile, Appointment, PatientProfile
from .forms import PatientSignUpForm, AppointmentForm, DoctorProfileForm


def home(request):
    return render(request, 'home.html')


@login_required
def patient_dashboard(request):
    patient = PatientProfile.objects.get(user=request.user)
    doctors = DoctorProfile.objects.all()
    appointments = Appointment.objects.filter(patient=patient)

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')

        if doctor_id and date and time and reason:
            doctor = DoctorProfile.objects.get(id=doctor_id)
            Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                date=date,
                time=time,
                reason=reason
            )
            messages.success(request, "Appointment booked successfully.")
            return redirect('patient_dashboard')

    context = {
        'patient': patient,
        'doctors': doctors,
        'appointments': appointments,
    }
    return render(request, 'patient_dashboard.html', context)



def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, 'patient_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'patient':
                return redirect('patient_dashboard')
            elif user.role == 'doctor':
                return redirect('doctor_dashboard')
            elif user.role == 'admin':
                return redirect('/admin/')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')


@login_required
def doctor_dashboard(request):
    doctor_profile = DoctorProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=doctor_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('doctor_dashboard')
    else:
        form = DoctorProfileForm(instance=doctor_profile)

    appointments = Appointment.objects.filter(doctor=doctor_profile).select_related('patient__user')

    return render(request, 'doctor_dashboard.html', {
        'form': form,
        'appointments': appointments
    })

@login_required
def book_appointment(request):
    if request.user.role != 'patient':
        return redirect('home')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patientprofile
            appointment.save()
            messages.success(request, "Appointment booked successfully.")
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})
