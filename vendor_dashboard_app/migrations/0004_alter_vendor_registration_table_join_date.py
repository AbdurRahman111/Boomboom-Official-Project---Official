# Generated by Django 3.2.6 on 2021-09-21 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_dashboard_app', '0003_alter_vendor_registration_table_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_registration_table',
            name='join_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 16, 35, 22, 140930)),
        ),
    ]
