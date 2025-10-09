from django import forms
from django.contrib import admin
from med_portal_backend.models import Patient, Medication


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = "__all__"


class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    list_display = ['first_name', 'last_name', 'dob', 'email']
    form = PatientForm


class MedicationAdmin(admin.ModelAdmin):
    list_filter = ['patient']
    search_fields = ['medication_name', 'medication_date']
    list_display = ['medication_name', 'medication_date', 'medication_type', 'medication_quantity', 'medication_unit']
    form = MedicationForm


admin.site.register(Patient, PatientAdmin)
admin.site.register(Medication, MedicationAdmin)
