from django.conf.urls import url
from . import views
from django.contrib.auth import login , logout
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserUpdate, Success

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login_success/$', views.login_success, name='login_success'),
    url(r'test/$', views.test, name='test'),
    url(r'doctor_list/$', views.doctor_list, name='doctor_list'),
    url(r'^doctor_home$', views.doctor_home, name='doctor_home'),
    url(r'^admin_home$', views.admin_home, name='admin_home'),
    url(r'^all_appointments$', views.all_appointments, name='all_appointments'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^doctor_register$', views.DoctorFormView.as_view(), name='doctor_register'),
    url(r'^login/$', LoginView.as_view(template_name = 'login.html'), name='login'),
    url(r'^appointment/add/$', views.AddAppointment, name='addappointment'),
    url(r'^appointment/(?P<pk>[0-9]+)/delete/$', views.AppointmentDelete.as_view(), name='deleteappointment'),
    url(r'^appointment/(?P<pk>[0-9]+)/$', views.AppointmentUpdate.as_view(), name='updateappointment'),
    url(r'^profile/edit/$', UserUpdate.as_view(), name='user-update'),
    url(r'^profile/edit/success$', Success, name='success'),
    url(r'^logout/$', LogoutView.as_view(next_page = '/index/login'), name='logout'),
]