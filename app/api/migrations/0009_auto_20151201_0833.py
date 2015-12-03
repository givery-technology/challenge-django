# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20151201_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
