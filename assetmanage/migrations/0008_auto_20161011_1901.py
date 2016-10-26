# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0007_auto_20161011_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='remote_ip',
            field=models.CharField(default=b'null', max_length=20),
        ),
        migrations.AlterField(
            model_name='assetmanage',
            name='server_ip',
            field=models.CharField(default=b'null', max_length=20),
        ),
    ]
