# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0013_auto_20170213_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkinfo',
            name='available_intf',
            field=models.CharField(default=b'-', max_length=100),
        ),
    ]
