# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasevehiculo',
            fields=[
                ('descripcion', models.CharField(max_length=60, null=True, blank=True)),
                ('idclasev', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'clasevehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Combustibles',
            fields=[
                ('nombrecomb', models.CharField(max_length=60, null=True, blank=True)),
                ('idcomb', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'combustibles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('nombreprov', models.CharField(max_length=60, null=True, blank=True)),
                ('idprov', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipovehiculo',
            fields=[
                ('nombretipov', models.CharField(max_length=60, null=True, blank=True)),
                ('idtipov', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'tipovehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('placa', models.CharField(max_length=15, null=True, blank=True)),
                ('modelo', models.CharField(max_length=6, null=True, blank=True)),
                ('marca', models.CharField(max_length=30, null=True, blank=True)),
                ('tonelaje', models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)),
                ('asientos', models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)),
                ('idvehiculo', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'vehiculos',
                'managed': False,
            },
        ),
    ]
