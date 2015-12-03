# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151201_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(max_length=50),
        ),
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
