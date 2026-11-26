from rest_framework import serializers
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.user.username', read_only=True)
    patient_name = serializers.CharField(source='patient.user.username', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'doctor',
            'doctor_name',
            'patient',
            'patient_name',
            'appointment_date',
            'appointment_time',
            'status',
            'reason',
            'created_at',
        ]
        read_only_fields = ['status', 'created_at']


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'doctor',
            'patient',
            'appointment_date',
            'appointment_time',
            'reason',
        ]

    def validate(self, data):
        # simple validation: doctor and patient must exist
        if not Doctor.objects.filter(id=data['doctor'].id).exists():
            raise serializers.ValidationError('Doctor not found')
        if not Patient.objects.filter(id=data['patient'].id).exists():
            raise serializers.ValidationError('Patient not found')
        return data