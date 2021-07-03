from django.shortcuts import render, redirect

from .forms import PatientForm
from .models import PatientInfor

def patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
    return render(request, 'hospital/patientform.html', {'form': form})

def report(name):
    patient = PatientInfor.objects.all
    lst = [p for p in patient if p[doctor_name] == name]
    return render (request,'hospital/patientinfor.html',lst)

    
def doctor(request):
    if request.method == "POST":
        name = request.POST['name']
        return report(name)
    return render(request,'hospital/doc.html')


