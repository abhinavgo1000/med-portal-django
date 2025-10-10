from django.db import models


class Physician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_name = models.CharField(max_length=100)
    diagnosis_description = models.TextField()

    class Meta:
        verbose_name_plural = "Diagnoses"

    def __str__(self):
        return self.diagnosis_name


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    medication_date = models.DateField()
    medication_type = models.CharField(max_length=100)
    medication_quantity = models.IntegerField()
    medication_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.medication_name + " " + self.medication_date


class PaymentMethod(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    is_insurance = models.BooleanField()
    insurance_provider = models.CharField(max_length=100, null=True, blank=True)
    insurance_number = models.CharField(max_length=100, null=True, blank=True)
    card_number = models.CharField(max_length=100, null=True, blank=True)
    card_expiry_month = models.IntegerField(null=True, blank=True)
    card_expiry_year = models.IntegerField(null=True, blank=True)
    card_security_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    billing_date = models.DateField()
    billing_amount = models.IntegerField()
    billing_due_date = models.DateField()
    billing_card_number = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name
