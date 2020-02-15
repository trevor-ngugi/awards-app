# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-15 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardss', '0007_projects_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['pub_date']},
        ),
        migrations.AddField(
            model_name='projects',
            name='project_image',
            field=models.ImageField(default=1, upload_to='project/'),
            preserve_default=False,
        ),
    ]