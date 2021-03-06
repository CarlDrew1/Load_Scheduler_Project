# Generated by Django 3.0.3 on 2020-02-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Runs', '0012_auto_20200226_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='permit',
            name='BC510',
            field=models.CharField(default='NO', max_length=10),
        ),
        migrations.AlterField(
            model_name='runs',
            name='trailer_1',
            field=models.CharField(choices=[('H180J', 'H180J'), ('FC505', 'FC505'), ('FC503', 'FC503'), ('FC504', 'FC504'), ('M441R', 'M441R'), ('Q738U', 'Q738U'), ('BC606', 'BC606'), ('BC604', 'BC604'), ('BC605', 'BC605'), ('BC607', 'BC607'), ('BC608', 'BC608'), ('BC602', 'BC602'), ('BC619', 'BC619'), ('BC603', 'BC603'), ('BC615', 'BC615'), ('BC620', 'BC620'), ('BC609', 'BC609'), ('NFC502', 'NFC502'), ('BC614', 'BC614'), ('BC621', 'BC621'), ('BC610', 'BC610'), ('BC622', 'BC622'), ('BC623', 'BC623'), ('TBC', 'TBC'), ('BC510', 'BC510')], max_length=50),
        ),
        migrations.AlterField(
            model_name='runs',
            name='truck',
            field=models.CharField(max_length=50),
        ),
    ]
