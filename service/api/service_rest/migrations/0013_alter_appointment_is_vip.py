# Generated by Django 4.0.3 on 2023-03-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0012_remove_appointment_status_appointment_is_finished_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='is_vip',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
