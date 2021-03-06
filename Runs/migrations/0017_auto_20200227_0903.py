# Generated by Django 3.0.3 on 2020-02-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Runs', '0016_auto_20200226_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runs',
            name='cubic',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='runs',
            name='foodstuffs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='runs',
            name='gib',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='runs',
            name='run_details',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='runs',
            name='trailer_1',
            field=models.CharField(choices=[('H180J', 'H180J'), ('FC505', 'FC505'), ('FC503', 'FC503'), ('FC504', 'FC504'), ('M441R', 'M441R'), ('Q738U', 'Q738U'), ('BC606', 'BC606'), ('BC604', 'BC604'), ('BC605', 'BC605'), ('BC607', 'BC607'), ('BC608', 'BC608'), ('BC602', 'BC602'), ('BC619', 'BC619'), ('BC603', 'BC603'), ('BC615', 'BC615'), ('BC620', 'BC620'), ('BC609', 'BC609'), ('NFC502', 'NFC502'), ('BC614', 'BC614'), ('BC621', 'BC621'), ('BC610', 'BC610'), ('BC622', 'BC622'), ('BC623', 'BC623'), ('TBC', 'TBC'), ('BC510', 'BC510'), ('A125', 'A125'), ('A125B', 'A125B'), ('ASJ583', 'ASJ583'), ('AZP219', 'AZP219'), ('B373J', 'B373J'), ('BC503', 'BC503'), ('BC506', 'BC506'), ('BC507', 'BC507'), ('BC509', 'BC509'), ('BC511', 'BC511'), ('BC516', 'BC516'), ('BC518', 'BC518'), ('BC601', 'BC601'), ('BCF001', 'BCF001'), ('BCF002', 'BCF002'), ('BCF004', 'BCF004'), ('BCF005', 'BCF005'), ('FC401', 'FC401'), ('FC402', 'FC402'), ('FC403', 'FC403'), ('FC404', 'FC404'), ('FC408', 'FC408'), ('FC409', 'FC409')], max_length=50),
        ),
        migrations.AlterField(
            model_name='runs',
            name='weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
