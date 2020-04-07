from django.db import models

# Create your models here.
from datetime import datetime
CHOICES = (
    ('Malaria', 'Malaria'),
    ('Covid 19', 'Covid 19'),
    ('Typhoid fever', 'Typhoid fever'),
    ('Kidney Stone', 'Kidney Stone'),
    ('Tooth Decay', 'Tooth Decay'),
)



class Registration(models.Model):
    patientName = models.CharField(max_length=100)
    patientNumber = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=100)
    patientcity = models.CharField(max_length=100)
    patientSex = models.CharField(max_length=100,   null=True, )
    
    patientDOB = models.DateTimeField(default=datetime.now())
    careNumber = models.CharField(max_length=100)
    MaritalStatus = models.CharField(max_length=100)
    sickness = models.CharField(max_length=100, choices=CHOICES, default='green')

    RegistrationLocation = models.CharField(max_length=100)

    doctorName = models.CharField(max_length=100)







