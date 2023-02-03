# Generated by Django 4.1.5 on 2023-02-03 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataglen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the error stream, should be unique for this source', max_length=128)),
                ('streamDataType', models.CharField(choices=[('INTEGER', 'Integer'), ('BOOLEAN', 'Boolean'), ('STRING', 'String'), ('FLOAT', 'Float'), ('LONG', 'Long'), ('MAC', 'Mac'), ('TIMESTAMP', 'Timestamp'), ('DATE', 'Date'), ('TIME', 'Time')], help_text='Type of the data this stream reports', max_length=20)),
                ('streamDateTimeFormat', models.CharField(blank=True, help_text='DateTime field values should be reported in ISO 8601 formats. You can specify custom formats here.', max_length=20)),
                ('streamPositionInCSV', models.IntegerField(blank=True, help_text='Applicable only if source dataFormat is CSV, should be unique', null=True)),
                ('streamDataUnit', models.CharField(blank=True, help_text='Data Unit', max_length=20, null=True)),
                ('multiplicationFactor', models.FloatField(default=1.0, help_text='Multiplication factor for this stream, applicable only for numerical streams. Defaults to one.')),
                ('isActive', models.BooleanField(default=True, help_text='If this data stream is active and accepting data.')),
                ('type', models.CharField(default='error', max_length=10)),
                ('source', models.ForeignKey(help_text='Key of the source this stream belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='errorfields', related_query_name='errorfield', to='dataglen.sensor', to_field='sourceKey')),
            ],
            options={
                'unique_together': {('source', 'streamPositionInCSV'), ('source', 'name')},
            },
        ),
    ]
