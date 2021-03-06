# Generated by Django 3.2.5 on 2021-09-29 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0018_auto_20210929_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 722751)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Order_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 722751)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 722751)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 722751)),
        ),
        migrations.AlterField(
            model_name='order_table_2',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 724748)),
        ),
        migrations.AlterField(
            model_name='order_table_3_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 731727)),
        ),
        migrations.AlterField(
            model_name='order_table_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 18, 59, 45, 730730)),
        ),
    ]
