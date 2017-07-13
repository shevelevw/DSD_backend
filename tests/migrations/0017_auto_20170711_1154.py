# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-11 11:54
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0016_auto_20170602_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', ckeditor.fields.RichTextField()),
                ('question_type', models.CharField(choices=[('RD', 'READING'), ('WR', 'WRITING'), ('LS', 'LISTENING')], default='RD', max_length=2)),
                ('rec_duration', models.IntegerField(default=1800)),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='topic',
        ),
        migrations.AlterField(
            model_name='test',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testlog',
            name='photo',
            field=models.ImageField(editable=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='testlog',
            name='screenshot',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='test',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tests.Question'),
        ),
    ]