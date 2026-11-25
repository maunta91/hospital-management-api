from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer, DoctorCreateSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DoctorCreateSerializer
        return DoctorSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
