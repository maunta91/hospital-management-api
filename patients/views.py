from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer, PatientCreateSerializer


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PatientCreateSerializer
        return PatientSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
