# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0005_auto_20161011_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='remote_ip',
            field=models.CharField(unique=True, max_length=20, blank=True),
        ),
    ]
