# Generated by Django 3.2.5 on 2021-09-25 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0009_auto_20210925_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign_table',
            name='end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 845029), null=True),
        ),
        migrations.AlterField(
            model_name='campaign_table',
            name='start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 845029), null=True),
        ),
        migrations.AlterField(
            model_name='customer_review',
            name='Review_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 843034)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 844031)),
        ),
        migrations.AlterField(
            model_name='flash_sell',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 844031)),
        ),
        migrations.AlterField(
            model_name='products',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 840042)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 840042)),
        ),
        migrations.AlterField(
            model_name='products',
            name='flash_sell_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 840042)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='First_Register_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 845029)),
        ),
        migrations.AlterField(
            model_name='staff_access',
            name='Last_login_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 11, 18, 54, 845029)),
        ),
    ]