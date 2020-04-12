# Generated by Django 2.2.5 on 2020-04-09 10:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, default='', max_length=500)),
                ('name', models.CharField(blank=True, max_length=500)),
                ('Address', models.CharField(default=None, max_length=100)),
                ('Email', models.CharField(default=None, max_length=100)),
                ('Phone', models.CharField(default=None, max_length=100)),
                ('gender', models.CharField(default=None, max_length=100)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='conuhospital.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Speciality', models.CharField(default=None, max_length=100)),
                ('days_of_work', models.CharField(default=None, max_length=100)),
                ('Email', models.CharField(default=None, max_length=100)),
                ('Phone', models.CharField(default=None, max_length=100)),
                ('hours_of_work', models.CharField(default=None, max_length=100)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='conuhospital.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='conuhospital.Doctor')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
