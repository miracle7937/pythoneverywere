

import django_filters
from .models import Registration
from django_filters import DateFilter, CharFilter, ChoiceFilter
from django import forms






class PatientFilter(django_filters.FilterSet):
    CHOICES = (
        ('Malaria', 'Malaria'),
        ('Covid 19', 'Covid 19'),
        ('Typhoid fever', 'Typhoid fever'),
        ('Kidney Stone', 'Kidney Stone'),
        ('Tooth Decay', 'Tooth Decay'),
    )
    patientName = CharFilter(field_name='patientName', lookup_expr='icontains',widget=forms.TextInput(attrs={'class':"form-control mb-2", 'id':"inlineFormInput", 'placeholder':"Name "}),)
    sickness = ChoiceFilter(field_name='sickness', lookup_expr='icontains', choices=CHOICES,
                            widget=forms.Select(attrs={'class': "form-control mb-2", 'id': "inlineFormInput", 'placeholder': "Sickness"}),)
    class Meta:
        model = Registration
        fields = ['patientName', 'sickness']
    
