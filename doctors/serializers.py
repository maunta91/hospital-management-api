from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor

User = get_user_model()


class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'id',
            'username',
            'email',
            'specialization',
            'experience_years',
            'consultation_fee',
        ]


class DoctorCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = [
            'username',
            'email',
            'password',
            'specialization',
            'experience_years',
            'consultation_fee',
        ]

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email', '')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='doctor',
        )
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor