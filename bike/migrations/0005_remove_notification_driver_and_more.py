# Generated by Django 4.1.5 on 2023-07-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_rename_rider_notification_driver_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='Driver',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='Passenger',
        ),
        migrations.AddField(
            model_name='driver',
            name='First_Name',
            field=models.CharField(default='DEFAULT', max_length=30),
        ),
        migrations.AddField(
            model_name='notification',
            name='Driver_Name',
            field=models.CharField(default='DEFAULT', max_length=30),
        ),
        migrations.AddField(
            model_name='notification',
            name='Driver_Phone',
            field=models.CharField(default='DEFAULT', max_length=15),
        ),
        migrations.AddField(
            model_name='notification',
            name='Passenger_Name',
            field=models.CharField(default='DEFAULT', max_length=30),
        ),
        migrations.AddField(
            model_name='notification',
            name='Passenger_Phone',
            field=models.CharField(default='DEFAULT', max_length=15),
        ),
        migrations.AddField(
            model_name='passenger',
            name='First_Name',
            field=models.CharField(default='DEFAULT', max_length=30),
        ),
        migrations.AlterField(
            model_name='driver',
            name='UserName',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='UserName',
            field=models.CharField(max_length=15),
        ),
    ]
