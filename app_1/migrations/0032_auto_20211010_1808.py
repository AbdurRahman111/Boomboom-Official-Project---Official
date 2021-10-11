# Generated by Django 3.2.5 on 2021-10-10 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0031_auto_20211010_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign_table',
            name='end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 307875), null=True),
        ),
        migrations.AlterField(
            model_name='campaign_table',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 307875), null=True),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='Review_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 288795)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 306847)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 306847)),
        ),
        migrations.AlterField(
            model_name='products',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 288795)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 288795)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 288795)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='First_Register_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 306847)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='Last_login_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 306847)),
        ),
    ]
