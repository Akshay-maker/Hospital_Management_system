from rest_framework.routers import SimpleRouter
from .views import PatientOperations, DoctorOperations, AppointmentOperations, PersonOperations

simpleRouter = SimpleRouter()

simpleRouter.register('person', PersonOperations)
simpleRouter.register('patient', PatientOperations)
simpleRouter.register('doctor', DoctorOperations)
simpleRouter.register('appointment', AppointmentOperations)


urlpatterns = simpleRouter.urls