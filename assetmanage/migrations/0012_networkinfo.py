# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0011_auto_20161104_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Networkinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_num', models.CharField(unique=True, max_length=50)),
                ('type_info', models.CharField(max_length=50)),
                ('server_ip', models.CharField(default=b'-', max_length=20)),
                ('data_center', models.CharField(max_length=50)),
                ('room_num', models.CharField(max_length=20)),
                ('rack_num', models.CharField(max_length=20)),
                ('asset_num', models.CharField(default=b'-', max_length=50)),
                ('module', models.CharField(default=b'-', max_length=50)),
                ('available_intf', models.CharField(default=b'-', max_length=100)),
                ('buy_time', models.CharField(default=b'-', max_length=50)),
                ('expiration_time', models.CharField(default=b'-', max_length=50)),
                ('note', models.CharField(default=b'-', max_length=200)),
            ],
        ),
    ]
