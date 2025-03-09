# Generated by Django 5.1.7 on 2025-03-09 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.FloatField()),
                ('precipitation', models.FloatField()),
                ('recorded_at', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='locations.location')),
            ],
        ),
    ]
