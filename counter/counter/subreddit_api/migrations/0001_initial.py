# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=600)),
                ('display_name_count', models.IntegerField()),
                ('title_count', models.IntegerField()),
                ('description_count', models.IntegerField()),
            ],
        ),
    ]
