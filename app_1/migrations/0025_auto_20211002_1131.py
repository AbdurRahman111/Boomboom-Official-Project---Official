# Generated by Django 3.2.6 on 2021-10-02 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0024_auto_20211001_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign_table',
            name='end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 804193), null=True),
        ),
        migrations.AlterField(
            model_name='campaign_table',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 804193), null=True),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='Review_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 800201)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 803194)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 803194)),
        ),
        migrations.AlterField(
            model_name='products',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 798206)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 798206)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 798206)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='First_Register_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 803194)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='Last_login_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 2, 11, 31, 34, 803194)),
        ),
    ]
