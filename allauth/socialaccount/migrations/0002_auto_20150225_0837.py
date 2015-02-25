# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialtoken',
            name='token',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='socialtoken',
            name='token_secret',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
