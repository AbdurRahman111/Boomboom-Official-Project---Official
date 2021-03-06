# Generated by Django 3.2.6 on 2021-09-21 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_auto_20210921_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign_table',
            name='end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 274078), null=True),
        ),
        migrations.AlterField(
            model_name='campaign_table',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 274078), null=True),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='Review_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 263663)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 274078)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 273043)),
        ),
        migrations.AlterField(
            model_name='products',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 263663)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 263663)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 263663)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='First_Register_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 274078)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='Last_login_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 21, 18, 29, 30, 274078)),
        ),
    ]
