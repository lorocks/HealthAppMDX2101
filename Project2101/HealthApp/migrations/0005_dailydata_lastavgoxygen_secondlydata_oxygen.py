# Generated by Django 4.0 on 2022-03-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0004_testingapi_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydata',
            name='LastAvgOxygen',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='secondlydata',
            name='Oxygen',
            field=models.FloatField(default=0),
        ),
    ]
