# Generated by Django 3.2.6 on 2021-10-01 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0022_auto_20211001_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Order_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
        migrations.AlterField(
            model_name='order_table_2',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
        migrations.AlterField(
            model_name='order_table_3_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
        migrations.AlterField(
            model_name='order_table_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 1, 19, 41, 39, 418554)),
        ),
    ]
