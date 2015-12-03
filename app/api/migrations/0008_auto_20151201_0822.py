# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20151201_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='company',
            field=models.CharField(default=b'defaultCompany', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(default=b'defaultLocation', max_length=50, null=True),
        ),
    ]
