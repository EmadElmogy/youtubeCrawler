# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.CharField(editable=False, max_length=150, primary_key=True, serialize=False, unique=True)),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('typ', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Playlist'), (1, 'Channel')], null=True)),
            ],
            options={
                'verbose_name': 'Content Source',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(editable=False, max_length=70, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=400)),
                ('duration', models.DurationField()),
                ('views_count', models.PositiveIntegerField()),
                ('thumbnail', models.URLField()),
                ('image', models.URLField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='youtubeCrawler.Source')),
            ],
        ),
    ]
