# Generated by Django 4.1.5 on 2023-02-08 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0002_alter_installation_install_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='install_ts',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 8, 12, 28, 45, 74465)),
        ),
    ]
