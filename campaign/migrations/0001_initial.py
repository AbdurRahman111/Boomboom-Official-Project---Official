# Generated by Django 3.2.5 on 2021-10-10 12:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_1', '0032_auto_20211010_1808'),
        ('vendor_dashboard_app', '0031_alter_vendor_registration_table_join_date'),
        ('checkout', '0031_auto_20211010_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor_notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification_text', models.TextField()),
                ('Notification_time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 326095))),
                ('Notification_stuff', models.ManyToManyField(blank=True, null=True, to='app_1.Staff_Access')),
                ('Notification_vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_dashboard_app.vendor_registration_table')),
            ],
            options={
                'verbose_name_plural': 'Vendor Notifications',
            },
        ),
        migrations.CreateModel(
            name='Order_notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification_text', models.TextField()),
                ('Notification_time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 18, 7, 57, 326095))),
                ('Notification_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.order_table')),
                ('Notification_stuff', models.ManyToManyField(blank=True, null=True, to='app_1.Staff_Access')),
            ],
            options={
                'verbose_name_plural': 'Order Notifications',
            },
        ),
    ]
