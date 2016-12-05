# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 21:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostLog',
            fields=[
                ('trigger_mode', models.CharField(max_length=10)),
                ('trigger_tuple', models.CharField(max_length=5)),
                ('trigger_changed', models.DateTimeField()),
                ('trigger_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('trigger_user', models.CharField(max_length=32)),
                ('mac', models.TextField()),
                ('hostname', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('address_type', models.IntegerField(blank=True, db_column=b'address_type_id', null=True)),
                ('dhcp_group', models.IntegerField(blank=True, null=True)),
                ('expires', models.DateTimeField()),
                ('changed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hosts_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PoolLog',
            fields=[
                ('trigger_mode', models.CharField(max_length=10)),
                ('trigger_tuple', models.CharField(max_length=5)),
                ('trigger_changed', models.DateTimeField()),
                ('trigger_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('trigger_user', models.CharField(max_length=32)),
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('allow_unknown', models.BooleanField(default=False)),
                ('lease_time', models.IntegerField()),
                ('dhcp_group', models.IntegerField(blank=True, null=True)),
                ('assignable', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'pools_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('to', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'db_table': 'email_log',
            },
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('trigger_mode', models.CharField(max_length=10)),
                ('trigger_tuple', models.CharField(max_length=5)),
                ('trigger_changed', models.DateTimeField()),
                ('trigger_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('trigger_user', models.CharField(max_length=32)),
                ('id', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('source', models.IntegerField()),
                ('min_permissions', models.BinaryField(max_length=8)),
                ('password', models.CharField(default=b'!', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_ipamadmin', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users_log',
                'managed': True,
            },
        ),
    ]
