from django import forms
from .models import PatientInfor


class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientInfor
        fields = '__all__'
