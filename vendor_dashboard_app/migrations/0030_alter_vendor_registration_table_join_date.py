# Generated by Django 3.2.5 on 2021-10-10 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_dashboard_app', '0029_alter_vendor_registration_table_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_registration_table',
            name='join_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 42, 763547)),
        ),
    ]
