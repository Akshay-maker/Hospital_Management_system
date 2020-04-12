import requests
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Appointment, Person, Doctor, User , Patient
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserForm, PatientForm, DoctorForm, PersonForm, UpdateForm
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


def test(request):
    return render(request, 'test.html')

BASE_URI = "http://127.0.0.1:8000/v1/appointment/"
@login_required(login_url='login')
def index(request):
    users = User.objects.all()
    print(users)
    appointments = Appointment.objects.filter(user=request.user)
    print(appointments)
    # app = requests.get(BASE_URI+str(users.id))
    # print(app)
    return render(request, 'index.html', {'appointments': appointments, 'Users': users})


@login_required(login_url='login')
def doctor_list(request):
    doctors = Doctor.objects.all()
    doc = requests.get("http://127.0.0.1:8000/v1/doctor/")
    print(doc.json())
    return render(request, 'doctor_list.html', {'doctors': doc.json()})



@login_required(login_url='login')
def doctor_home(request):
    user = request.user
    person = Person.objects.get(user=user)
    doctor = Doctor.objects.get(person=person)
    appointments = Appointment.objects.filter(Doctor=doctor)
    print("##", appointments)
    # app = requests.get("http://127.0.0.1:8000/v1/appointment/"+str(doctor.id))
    return render(request, 'doctor_home.html', {'appointments': appointments})



@login_required(login_url='login')
def admin_home(request):
    return render(request, 'admin_home.html')



class UserFormView(View):

    user_form_class = UserForm
    patient_form_class = PatientForm
    template_name = 'registration.html'

    #show blank forqm

    def get(self, request):
        u_form = self.user_form_class(None)
        p_form = self.patient_form_class(None)
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form})

    #register user

    def post(self , request):
        u_form = self.user_form_class(request.POST)
        p_form = self.patient_form_class(request.POST)
        if u_form.is_valid() and p_form.is_valid():

            #save user info locally and not in the database yet
            user = u_form.save(commit=False)
            patient = p_form.save(commit=False)

            #cleaned data
            username = u_form.cleaned_data['username']
            password = u_form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value
            user.set_password(password)
            user.save()

            person = Person(user=user)

            person.save()

            #save info to DB
            patient.person = Person.objects.get(user=user)
            patient.save()

            user = authenticate(username=username , password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect('index.html')

        # if fails , then return form
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form})


class DoctorFormView(View):

    user_form_class = UserForm
    doctor_form_class = DoctorForm
    person_form_class = PersonForm
    template_name = 'doctor_registration.html'

    #show blank forqm

    def get(self, request):
        u_form = self.user_form_class(None)
        p_form = self.person_form_class(None)
        d_form = self.doctor_form_class(None)
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form,  'd_form': d_form})

    #register user

    def post(self , request):
        u_form = self.user_form_class(request.POST)
        p_form = self.person_form_class(request.POST)
        d_form = self.doctor_form_class(request.POST)
        if u_form.is_valid() and d_form.is_valid() and p_form.is_valid():

            #save user info locally and not in the database yet
            user = u_form.save(commit=False)
            doctor = d_form.save(commit=False)
            person = p_form.save(commit=False)

            #cleaned data

            username = u_form.cleaned_data['username']
            password = u_form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value
            user.set_password(password)
            user.save()
            person.save()


            person = Person.objects.get(user=user)
            person.type=1
            person.save()


            #save info to DB
            doctor.person = Person.objects.get(user=user)
            app = requests.post("http://127.0.0.1:8000/v1/appointment/", data=doctor)
            # doctor.save()
            return redirect('admin_home.html')

        # if fails , then return form
        return render(request, self.template_name, {'u_form' : u_form , 'd_form' : d_form})


@login_required(login_url='login')
def login_success(request):
    if request.user.is_superuser:
        return redirect("admin_home.html")
    person=Person.objects.get(user=request.user)
    if person.type == 1:
        return redirect("doctor_home.html")
    else:
        return redirect("index.html")


@login_required(login_url='login')
def AddAppointment(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            appointments = Appointment.objects.filter(user=request.user)
            return render(request, 'index.html', {'appointments': appointments})
        context = {
                "form": form,
            }
    return render(request, 'appointment_form.html', context)


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('index.html')


class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['user', 'Doctor', 'Date', 'status', 'message']
    success_url = 'success'


class UserUpdate(UpdateView):

    context_object_name = 'form'
    form_class = PatientForm
    template_name = 'userupdate.html'
    success_url = 'success'

    # get object
    def get_object(self, queryset=None):
        person = Person.objects.get(user=self.request.user)
        return Patient.objects.get(person=person)

    # override form_valid method
    def form_valid(self, form):
        # save cleaned post data
        clean = form.cleaned_data
        self.object = form.save(clean)
        return super(UserUpdate, self).form_valid(form)

def Success(request):
    return render(request, 'success.html')


def all_appointments(request):
    # appointments = Appointment.objects.all()
    app = requests.get("http://127.0.0.1:8000/v1/appointment/")
    return render(request, 'all_appointments.html', {'appointments': app})
