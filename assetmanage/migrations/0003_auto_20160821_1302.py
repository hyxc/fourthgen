# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0002_auto_20160819_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='asset_num',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='assetmanage',
            name='remote_ip',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='assetmanage',
            name='server_ip',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='assetmanage',
            name='service_num',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='host_name',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='local_ip',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
