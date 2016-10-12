# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0008_auto_20161011_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='remote_ip',
            field=models.CharField(default=b'0.0.0.0', max_length=20),
        ),
        migrations.AlterField(
            model_name='assetmanage',
            name='server_ip',
            field=models.CharField(default=b'0.0.0.0', max_length=20),
        ),
    ]
