# Generated by Django 3.0.2 on 2020-01-24 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Runs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='runs',
            name='Planned_depart_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
