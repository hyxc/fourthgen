# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assetmanage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_num', models.CharField(max_length=50)),
                ('device_type', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('local_ip', models.CharField(max_length=20)),
                ('remote_ip', models.CharField(max_length=20)),
                ('system_type', models.CharField(max_length=20)),
                ('disksize', models.CharField(max_length=10)),
                ('dicknum', models.IntegerField()),
                ('diskraid', models.CharField(max_length=10)),
            ],
        ),
    ]
