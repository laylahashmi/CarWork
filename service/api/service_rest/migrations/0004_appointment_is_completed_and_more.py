# Generated by Django 4.0.3 on 2023-03-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0003_remove_appointment_date_remove_appointment_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='technician',
            name='employee_id',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
