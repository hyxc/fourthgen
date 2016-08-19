# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanage',
            name='server_ip',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='host_ip',
            field=models.ForeignKey(related_name='asset_set', to='assetmanage.Assetmanage'),
        ),
    ]
