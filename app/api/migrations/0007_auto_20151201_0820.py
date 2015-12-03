# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151201_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
