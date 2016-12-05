# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(b'feature', b'Feature'), (b'bug', b'Bug'), (b'comment', b'Comment')], max_length=255, verbose_name=b'Request Type')),
                ('comment', models.TextField(verbose_name=b'Comment Details')),
                ('submitted', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Submitted')),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-submitted',),
                'db_table': 'feature_requests',
            },
        ),
    ]
