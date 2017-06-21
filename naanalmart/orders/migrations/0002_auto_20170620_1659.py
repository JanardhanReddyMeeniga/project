# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docketnumbers',
            name='id',
        ),
        migrations.AlterField(
            model_name='docketnumbers',
            name='docket_number',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
