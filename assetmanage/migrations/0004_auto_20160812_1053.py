# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0003_auto_20160726_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetmanage',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='assetmanage',
            name='disknum',
        ),
        migrations.RemoveField(
            model_name='assetmanage',
            name='diskraid',
        ),
        migrations.RemoveField(
            model_name='assetmanage',
            name='disksize',
        ),
        migrations.RemoveField(
            model_name='assetmanage',
            name='type',
        ),
    ]
