# Generated by Django 4.0 on 2021-12-23 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIDs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('DoctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='HealthApp.userids')),
                ('Name', models.CharField(max_length=100)),
                ('ContactNum', models.CharField(max_length=12)),
                ('Hospital', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='HealthApp.userids')),
                ('Name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('Address', models.CharField(max_length=150)),
                ('ContactNum', models.CharField(max_length=12)),
                ('EmergencyContact', models.CharField(max_length=12)),
                ('Insurance', models.CharField(max_length=50)),
                ('EmailID', models.CharField(max_length=100)),
                ('DoctorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthApp.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('username', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('userType', models.CharField(choices=[('D', 'Doctor'), ('P', 'Patient')], max_length=1)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='userids',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthApp.usertype'),
        ),
        migrations.CreateModel(
            name='WeeklyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Weight', models.FloatField()),
                ('Height', models.FloatField()),
                ('BMI', models.FloatField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthApp.patients')),
            ],
        ),
        migrations.CreateModel(
            name='SecondlyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Pulse', models.FloatField()),
                ('Temp', models.FloatField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthApp.patients')),
            ],
        ),
        migrations.CreateModel(
            name='DailyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('LastAvgTemp', models.FloatField()),
                ('LastAvgHeartRate', models.FloatField()),
                ('BloodSugar', models.FloatField()),
                ('BloodPressure', models.FloatField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthApp.patients')),
            ],
        ),
    ]
