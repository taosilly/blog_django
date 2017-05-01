# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-01 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170501_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='describe',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='modified_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
