# Generated by Django 2.2.4 on 2019-08-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AddressLog",
            fields=[
                ("trigger_mode", models.CharField(max_length=10)),
                ("trigger_tuple", models.CharField(max_length=5)),
                ("trigger_changed", models.DateTimeField()),
                (
                    "trigger_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("trigger_user", models.CharField(max_length=32)),
                ("address", models.GenericIPAddressField()),
                ("mac", models.TextField(blank=True)),
                ("pool", models.IntegerField()),
                ("reserved", models.BooleanField()),
                ("network", models.TextField(blank=True)),
                ("changed", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "addresses_log", "managed": False},
        ),
        migrations.CreateModel(
            name="DnsRecordsLog",
            fields=[
                ("trigger_mode", models.CharField(max_length=10)),
                ("trigger_tuple", models.CharField(max_length=5)),
                ("trigger_changed", models.DateTimeField()),
                (
                    "trigger_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("trigger_user", models.CharField(max_length=32)),
                ("id", models.IntegerField()),
                ("domain", models.IntegerField(db_column="did")),
                ("type_id", models.IntegerField(db_column="tid")),
                ("dns_view", models.IntegerField(db_column="vid")),
                ("name", models.CharField(max_length=255)),
                (
                    "text_content",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("ip_content", models.TextField(blank=True, null=True)),
                ("ttl", models.IntegerField(blank=True, null=True)),
                ("priority", models.IntegerField(blank=True, null=True)),
                ("changed", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "dns_records_log", "managed": False},
        ),
        migrations.CreateModel(
            name="HostLog",
            fields=[
                ("trigger_mode", models.CharField(max_length=10)),
                ("trigger_tuple", models.CharField(max_length=5)),
                ("trigger_changed", models.DateTimeField()),
                (
                    "trigger_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("trigger_user", models.CharField(max_length=32)),
                ("mac", models.TextField()),
                ("hostname", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "address_type",
                    models.IntegerField(
                        blank=True, db_column="address_type_id", null=True
                    ),
                ),
                ("dhcp_group", models.IntegerField(blank=True, null=True)),
                ("expires", models.DateTimeField()),
                ("changed", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "hosts_log", "managed": False},
        ),
        migrations.CreateModel(
            name="PoolLog",
            fields=[
                ("trigger_mode", models.CharField(max_length=10)),
                ("trigger_tuple", models.CharField(max_length=5)),
                ("trigger_changed", models.DateTimeField()),
                (
                    "trigger_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("trigger_user", models.CharField(max_length=32)),
                ("id", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("allow_unknown", models.BooleanField(default=False)),
                ("lease_time", models.IntegerField()),
                ("dhcp_group", models.IntegerField(blank=True, null=True)),
                ("assignable", models.BooleanField(default=False)),
            ],
            options={"db_table": "pools_log", "managed": False},
        ),
        migrations.CreateModel(
            name="UserLog",
            fields=[
                ("trigger_mode", models.CharField(max_length=10)),
                ("trigger_tuple", models.CharField(max_length=5)),
                ("trigger_changed", models.DateTimeField()),
                (
                    "trigger_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("trigger_user", models.CharField(max_length=32)),
                ("id", models.IntegerField()),
                ("username", models.CharField(max_length=50)),
                (
                    "source_id",
                    models.IntegerField(blank=True, db_column="source", null=True),
                ),
                ("password", models.CharField(default="!", max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
                ("date_joined", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"db_table": "users_log", "managed": False},
        ),
        migrations.CreateModel(
            name="AuthSource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, unique=True)),
            ],
            options={"db_table": "auth_sources_log"},
        ),
        migrations.CreateModel(
            name="EmailLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("when", models.DateTimeField(auto_now_add=True)),
                ("to", models.EmailField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
            ],
            options={"db_table": "email_log"},
        ),
    ]
