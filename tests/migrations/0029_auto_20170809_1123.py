# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0028_auto_20170808_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='attachment',
            old_name='file_name',
            new_name='name',
        ),
    ]
