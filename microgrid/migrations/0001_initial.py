# Generated by Django 4.1.5 on 2023-02-08 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solarrms', '0001_initial'),
        ('dataglen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeController',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dataglen.sensor')),
                ('is_master', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charge_controllers', to='solarrms.solarplant')),
            ],
            bases=('dataglen.sensor',),
        ),
        migrations.CreateModel(
            name='PanelSet',
            fields=[
                ('independentinverter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='solarrms.independentinverter')),
                ('no_of_panels', models.IntegerField(default=1)),
                ('charge_controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panel_sets', to='microgrid.chargecontroller')),
            ],
            bases=('solarrms.independentinverter',),
        ),
        migrations.CreateModel(
            name='ConnectedLoad',
            fields=[
                ('independentinverter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='solarrms.independentinverter')),
                ('load_voltage', models.FloatField()),
                ('charge_controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_loads', to='microgrid.chargecontroller')),
            ],
            bases=('solarrms.independentinverter',),
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('independentinverter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='solarrms.independentinverter')),
                ('controllable', models.BooleanField(default=False)),
                ('charge_controller', models.ManyToManyField(related_name='batteries', to='microgrid.chargecontroller')),
            ],
            bases=('solarrms.independentinverter',),
        ),
    ]
