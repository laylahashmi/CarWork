# Generated by Django 4.0.3 on 2023-03-10 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0016_alter_appointment_is_vip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='is_vip',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='automobilevo',
            name='vin',
            field=models.CharField(max_length=17),
        ),
    ]