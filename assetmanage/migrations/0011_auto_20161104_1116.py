# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0010_auto_20161011_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='cpu_num',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='disk_size',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='host_name',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='mem_size',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='system_version',
        ),
    ]
