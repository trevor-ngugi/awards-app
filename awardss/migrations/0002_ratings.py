# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-15 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
            ],
        ),
    ]
