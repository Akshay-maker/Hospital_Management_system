from .models import Patient, Doctor, Appointment, Person
from .serializers import PatientSerialization, DoctorSerialization, AppointmentSerialization, PersonSerialization
from rest_framework.viewsets import ModelViewSet


class PatientOperations(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerialization


class DoctorOperations(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerialization


class AppointmentOperations(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerialization


class PersonOperations(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerialization