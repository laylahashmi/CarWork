# Generated by Django 4.0.3 on 2023-03-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0007_remove_appointment_date_time_appointment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]