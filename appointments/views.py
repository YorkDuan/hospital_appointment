from django.shortcuts import render
from .models import Doctor, Appointment  # Assuming your models are in the same directory


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


def appointment_list(request):
    # Assuming you have authenticated users and want to filter appointments for the current user
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})