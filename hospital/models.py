from django.db import models


class PatientInfor(models.Model):
    patient_name = models.CharField(max_length=200, null=False)
    patient_age = models.IntegerField(default=0)
    Issue = models.CharField(max_length=500,null=False)
    doctor_name = models.CharField(max_length=500,null=False)
    
    
