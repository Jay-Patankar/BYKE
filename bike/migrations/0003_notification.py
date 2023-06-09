# Generated by Django 4.1.5 on 2023-02-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_driver_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Source', models.CharField(max_length=300)),
                ('Destination', models.CharField(max_length=300)),
                ('fare', models.IntegerField()),
                ('DateTime', models.DateTimeField()),
                ('Rider', models.CharField(max_length=30)),
                ('Passenger', models.CharField(max_length=30)),
            ],
        ),
    ]
