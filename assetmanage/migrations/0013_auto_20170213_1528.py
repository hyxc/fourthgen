# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0012_networkinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkinfo',
            name='available_intf',
            field=models.CharField(max_length=100),
        ),
    ]
