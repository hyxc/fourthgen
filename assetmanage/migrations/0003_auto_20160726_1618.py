# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0002_auto_20160726_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetmanage',
            old_name='dicknum',
            new_name='disknum',
        ),
    ]
