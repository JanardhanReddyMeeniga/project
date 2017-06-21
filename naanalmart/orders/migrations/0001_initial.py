# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocketNumbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docket_number', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('orderno', models.CharField(max_length=100)),
                ('no_of_packages', models.IntegerField()),
                ('from_pkg_no', models.IntegerField()),
                ('to_pkg_no', models.IntegerField()),
                ('docketno', models.ForeignKey(related_name='docket', to='orders.DocketNumbers')),
                ('seller', models.ForeignKey(related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('package_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('length', models.IntegerField()),
                ('breadth', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('order', models.ForeignKey(related_name='order', to='orders.Orders')),
            ],
        ),
    ]
