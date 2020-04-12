from rest_framework.serializers import ModelSerializer
from .models import Patient, Doctor, Appointment, Person


class PatientSerialization(ModelSerializer):

    class Meta:
        model = Patient
        exclude = ('person',)


class DoctorSerialization(ModelSerializer):

    class Meta:
        model = Doctor
        exclude = ('person',)


class AppointmentSerialization(ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'



class PersonSerialization(ModelSerializer):

    class Meta:
        model = Person
        fields = ('type',)