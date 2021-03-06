# Generated by Django 3.2.6 on 2021-09-20 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_table_3',
            name='old_order_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 20, 13, 39, 36, 908752)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Order_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 20, 13, 39, 36, 908752)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 20, 13, 39, 36, 908752)),
        ),
        migrations.AlterField(
            model_name='order_table',
            name='Paid_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 20, 13, 39, 36, 908752)),
        ),
        migrations.AlterField(
            model_name='order_table_2',
            name='Order_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 20, 13, 39, 36, 908752)),
        ),
        migrations.AlterField(
            model_name='order_table_logs',
            name='logs_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 20, 13, 39, 36, 924340)),
        ),
    ]
