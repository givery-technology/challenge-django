# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151201_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.DateField(default=b'1991-04-13'),
        ),
        migrations.AlterField(
            model_name='users',
            name='company',
            field=models.CharField(default=b'defaultCompany', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(default=b'defaultLocation', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default=b'password', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default=b'defaultUser', max_length=100),
        ),
    ]
