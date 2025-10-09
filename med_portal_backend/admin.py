from django import forms
from django.contrib import admin
from med_portal_backend.models import Physician, Patient, Medication, Diagnosis


class PhysicianForm(forms.ModelForm):
    class Meta:
        model = Physician
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = "__all__"


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = "__all__"


class PhysicianAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'specialty']
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name']
    form = PhysicianForm


class PatientAdmin(admin.ModelAdmin):
    list_filter = ['first_name']
    search_fields = ['first_name', 'last_name', 'email']
    list_display = ['first_name', 'last_name', 'dob', 'email']
    form = PatientForm


class DiagnosisAdmin(admin.ModelAdmin):
    list_filter = ['patient']
    search_fields = ['diagnosis_name']


class MedicationAdmin(admin.ModelAdmin):
    list_filter = ['patient']
    search_fields = ['medication_name', 'medication_date']
    list_display = ['medication_name', 'medication_date', 'medication_type', 'medication_quantity', 'medication_unit']
    form = MedicationForm


admin.site.register(Physician, PhysicianAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Medication, MedicationAdmin)
