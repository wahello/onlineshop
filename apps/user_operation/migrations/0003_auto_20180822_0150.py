# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-22 01:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20171225_0630'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0002_auto_20171222_1942'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together=set([('user', 'goods')]),
        ),
    ]