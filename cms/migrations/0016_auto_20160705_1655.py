# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20160629_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='所属栏目', to='cms.Channel'),
        ),
    ]