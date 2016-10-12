# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0003_auto_20160821_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='remote_ip',
            field=models.CharField(max_length=20, unique=True, null=True),
        ),
    ]
