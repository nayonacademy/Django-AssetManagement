# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0004_assetdistribution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetdistribution',
            name='MemberName',
        ),
        migrations.AddField(
            model_name='assetdistribution',
            name='name',
            field=models.CharField(default='nayon', max_length=50),
            preserve_default=False,
        ),
    ]
