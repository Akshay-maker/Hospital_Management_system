# Hospital_Management_system

myhmsys >> Hospital Management system producer 
myhmscons >> Hospital Management System consumer


The myhmsys defines the Hospital management system project based on DJANGO REST FRAMEWORK
Allow it run with python manage.py runserver
The project defines swagger UI schema at http://127.0.0.1:8000/


The myhmscons defines the Hospital management system project which consumes myhmsys
Allow it run with python manage.py runserver 8001
The project defines HTML UI at http://127.0.0.1:8001/

Credentials to login:
ADMIN >> USERNAME: akshay   PASSWORD: akshay123
user >> USERNAME: drwho   PASSWORD: doctorwho

The user needs to register as person.
The person can be a patient or doctor. That has to be decided through admin login credentials.

Current Development:
1. At current the UI allows the user to login, register, edit profile 
2. Allows to get doctors list based on django drf
3. Allows to book appointment(need to work more)


