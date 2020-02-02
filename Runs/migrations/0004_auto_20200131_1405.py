# Generated by Django 3.0.2 on 2020-01-31 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Runs', '0003_back_trailer_front_trailer_routes'),
    ]

    operations = [
        migrations.AddField(
            model_name='runs',
            name='finished_loading_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='runs',
            name='run',
            field=models.CharField(choices=[('FCC', 'FCC'), ('CHC1', 'CHC1'), ('CHC2', 'CHC2'), ('CHC3', 'CHC3'), ('CHC4', 'CHC4'), ('CHC6', 'CHC6'), ('CHIG', 'CHIG'), ('FCI', 'FCI'), ('CHI', 'CHI'), ('CHI2', 'CHI2'), ('FCD', 'FCD'), ('CHD1', 'CHD1'), ('CHD2', 'CHD2'), ('CHD3', 'CHD3'), ('CHD4', 'CHD4'), ('CBN', 'CBN'), ('CBN1', 'CBN1'), ('CHN', 'CHN'), ('CHN1', 'CHN1'), ('CHN2', 'CHN2'), ('FCT', 'FCT'), ('CHT1', 'CHT1'), ('CHT2', 'CHT2'), ('CHW', 'CHW'), ('CHW1', 'CHW1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='runs',
            name='trailer_1',
            field=models.CharField(choices=[('H180J', 'H180J'), ('FC505', 'FC505'), ('FC503', 'FC503'), ('FC504', 'FC504'), ('M441R', 'M441R'), ('Q738U', 'Q738U'), ('BC606', 'BC606'), ('BC604', 'BC604'), ('BC605', 'BC605'), ('BC607', 'BC607'), ('BC608', 'BC608'), ('BC602', 'BC602'), ('BC619', 'BC619'), ('BC603', 'BC603'), ('BC615', 'BC615'), ('BC620', 'BC620'), ('BC609', 'BC609'), ('NFC502', 'NFC502'), ('BC614', 'BC614'), ('BC621', 'BC621'), ('BC610', 'BC610'), ('BC622', 'BC622'), ('BC623', 'BC623'), ('TBC', 'TBC')], max_length=50),
        ),
    ]