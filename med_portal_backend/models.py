from django.db import models


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

    def __str__(self):
        return self.first_name + " " + self.last_name


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    medication_date = models.DateField()
    medication_type = models.CharField(max_length=100)
    medication_quantity = models.IntegerField()
    medication_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.medication_name + " " + self.medication_date
