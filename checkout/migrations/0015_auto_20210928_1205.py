# Generated by Django 3.2.5 on 2021-09-28 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20210928_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_table',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 12, 5, 7, 900481)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Order_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 28, 12, 5, 7, 900481)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 12, 5, 7, 900481)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 28, 12, 5, 7, 900481)),
        ),
        migrations.AlterField(
            model_name='order_table_2',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 12, 5, 7, 901478)),
        ),
        migrations.AlterField(
            model_name='order_table_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 28, 12, 5, 7, 903472)),
        ),
    ]
