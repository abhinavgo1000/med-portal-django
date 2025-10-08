from django import forms
from django.contrib import admin
from med_portal_backend.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class MedPortalAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    list_display = ['first_name', 'last_name', 'dob', 'email']
    form = PatientForm


admin.site.register(Patient, MedPortalAdmin)
