from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    STATUS_CHOICES = (

        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),

    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='appointments')
    appointment_date = models.DateTimeField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.get_full_name()} for {self.patient.user.get_full_name()} on {self.appointment_date.strftime('%Y-%m-%d')} at {self.appointment_time.strftime('%H:%M')}"

# Create your models here.
