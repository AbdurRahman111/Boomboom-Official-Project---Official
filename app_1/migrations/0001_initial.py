# Generated by Django 3.2.6 on 2021-09-19 12:37

import ckeditor.fields
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor_dashboard_app', '__first__'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('old_customer_uniqe_id', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribute_name', models.CharField(max_length=100)),
                ('Attribute_slag', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Attribute_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='attribute_connect_with_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(blank=True, max_length=90, null=True)),
                ('Color', models.CharField(blank=True, max_length=90, null=True)),
                ('Flavor', models.CharField(blank=True, max_length=90, null=True)),
                ('Variation', models.CharField(blank=True, max_length=90, null=True)),
                ('Weight', models.CharField(blank=True, max_length=90, null=True)),
                ('Volume', models.CharField(blank=True, max_length=90, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=90, null=True)),
                ('Values', models.CharField(blank=True, max_length=90, null=True)),
                ('Material_Type', models.CharField(blank=True, max_length=90, null=True)),
                ('Product_Type', models.CharField(blank=True, max_length=90, null=True)),
                ('Verification', models.CharField(blank=True, max_length=90, null=True)),
                ('Quality', models.CharField(blank=True, max_length=90, null=True)),
                ('Marketing_Claims', models.CharField(blank=True, max_length=90, null=True)),
                ('Design', models.CharField(blank=True, max_length=90, null=True)),
                ('Smell', models.CharField(blank=True, max_length=90, null=True)),
                ('Reliability', models.CharField(blank=True, max_length=90, null=True)),
                ('Content', models.CharField(blank=True, max_length=90, null=True)),
                ('Safety', models.CharField(blank=True, max_length=90, null=True)),
                ('Package', models.CharField(blank=True, max_length=90, null=True)),
                ('Model', models.CharField(blank=True, max_length=90, null=True)),
                ('Taste', models.CharField(blank=True, max_length=90, null=True)),
                ('Feel', models.CharField(blank=True, max_length=90, null=True)),
                ('Defferent_Type', models.CharField(blank=True, max_length=90, null=True)),
                ('attribute_image_of_product', models.ImageField(blank=True, null=True, upload_to='')),
                ('Cost_Price', models.IntegerField(blank=True, null=True)),
                ('MRP_Price', models.IntegerField(blank=True, null=True)),
                ('Discount_Price', models.IntegerField(blank=True, null=True)),
                ('Attribute_Quantity', models.IntegerField(blank=True, null=True)),
                ('Stock_status', models.CharField(choices=[('In stock', 'In stock'), ('Out stock', 'Out stock'), ('On backorder', 'On backorder')], default='In stock', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Brand_Name', models.CharField(max_length=255)),
                ('Description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Brand_logo', models.ImageField(blank=True, null=True, upload_to='Brand_logo/')),
                ('Featured_Brand', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='campaign_categories_percentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(blank=True, null=True)),
                ('total_quantity_of_sell_cat_campaign', models.IntegerField(blank=True, null=True)),
                ('total_money_of_sell_cat_campaign', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'campaign_categories_percentage',
            },
        ),
        migrations.CreateModel(
            name='campaign_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_slug', models.CharField(max_length=255)),
                ('campaign_name', models.CharField(max_length=255)),
                ('start_time', models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848), null=True)),
                ('end_time', models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848), null=True)),
                ('campaign_logo', models.ImageField(blank=True, null=True, upload_to='campaign_logo/')),
                ('campaign_benner', models.ImageField(blank=True, null=True, upload_to='campaign_benner/')),
                ('finish_campaign', models.BooleanField(default=False)),
                ('free_delivery', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'campaign_table',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Slug', models.CharField(blank=True, max_length=255, null=True)),
                ('Category_Name', models.CharField(max_length=255)),
                ('Category_title', models.CharField(blank=True, max_length=255, null=True)),
                ('Category_discription', models.TextField(blank=True, null=True)),
                ('total_quantity_of_sell', models.IntegerField(blank=True, null=True)),
                ('total_money_of_sell', models.IntegerField(blank=True, null=True)),
                ('total_quantity_of_sell_reguler', models.IntegerField(blank=True, null=True)),
                ('total_money_of_sell_reguler', models.IntegerField(blank=True, null=True)),
                ('Category_benner', models.FileField(blank=True, help_text='Choose Only .jpg, .jpeg, .png and files PLease..', null=True, upload_to='Category_benner', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Flash_Sell',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('flash_sell_start_time', models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
                ('flash_sell_end_time', models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
            ],
            options={
                'verbose_name_plural': 'Flash Sell',
            },
        ),
        migrations.CreateModel(
            name='Staff_Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Staff_Role', models.CharField(choices=[('Admin', 'Admin'), ('Shop Manager', 'Shop Manager'), ('Customer Support', 'Customer Support'), ('Upload Team', 'Upload Team')], default='Admin', max_length=20)),
                ('First_Register_Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
                ('Last_login_Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
            ],
            options={
                'verbose_name_plural': 'Staff Access',
            },
        ),
        migrations.CreateModel(
            name='Subcategory_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subcategory_1', models.CharField(max_length=255)),
                ('add_home', models.BooleanField(default=False)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.category')),
            ],
            options={
                'verbose_name_plural': 'Subcategory_1',
            },
        ),
        migrations.CreateModel(
            name='Subcategory_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subcategory_2', models.CharField(max_length=255)),
                ('Subcategory_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.subcategory_1')),
            ],
            options={
                'verbose_name_plural': 'Subcategory_2',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Product_slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('Product_Name', models.CharField(max_length=255)),
                ('SKU', models.CharField(blank=True, max_length=255, null=True)),
                ('TYPE_OF_PRODUCTS', models.CharField(blank=True, max_length=20, null=True)),
                ('Cost_Price', models.IntegerField(blank=True, null=True)),
                ('MRP_Price', models.IntegerField(blank=True, null=True)),
                ('Discount_Price', models.IntegerField(blank=True, null=True)),
                ('Discount_Percentage', models.IntegerField(blank=True, null=True)),
                ('KG_or_Liter', models.IntegerField(blank=True, null=True)),
                ('Product_Description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Long_Product_Description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Meta_Title', models.CharField(blank=True, max_length=255, null=True)),
                ('Meta_Keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('Product_Image', models.TextField(blank=True, max_length=255, null=True)),
                ('Product_Image2', models.TextField(blank=True, max_length=255, null=True)),
                ('Product_Image3', models.TextField(blank=True, max_length=255, null=True)),
                ('Product_Image4', models.TextField(blank=True, max_length=255, null=True)),
                ('Stock_status', models.CharField(choices=[('In stock', 'In stock'), ('Out stock', 'Out stock'), ('On backorder', 'On backorder')], default='In stock', max_length=20)),
                ('Product_stock_Quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
                ('make_star', models.BooleanField(default=False)),
                ('flash_sell', models.BooleanField(default=False)),
                ('flash_sell_start_time', models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
                ('flash_sell_end_time', models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
                ('Review_Quantity', models.IntegerField(blank=True, null=True)),
                ('total_quantity_of_sell_product', models.IntegerField(blank=True, null=True)),
                ('total_money_of_sell_product', models.IntegerField(blank=True, null=True)),
                ('total_quantity_of_sell_reguler_product', models.IntegerField(blank=True, null=True)),
                ('total_money_of_sell_reguler_product', models.IntegerField(blank=True, null=True)),
                ('Brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.brand')),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.category')),
                ('Subcategory_1', models.ManyToManyField(blank=True, null=True, to='app_1.Subcategory_1')),
                ('Subcategory_2', models.ManyToManyField(blank=True, null=True, to='app_1.Subcategory_2')),
                ('Vendors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_dashboard_app.vendor_registration_table')),
                ('product_wishlist', models.ManyToManyField(blank=True, default=None, null=True, related_name='product_wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='customer_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ratting_qty', models.IntegerField()),
                ('Review_Text', models.TextField(blank=True, null=True)),
                ('Review_Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 19, 18, 37, 37, 443848))),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.products')),
            ],
            options={
                'verbose_name_plural': 'Customer Review',
            },
        ),
        migrations.CreateModel(
            name='campaign_product_table',
            fields=[
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('make_campaign_star', models.BooleanField(default=False)),
                ('make_index_star', models.BooleanField(default=False)),
                ('add_item_campaign', models.BooleanField(default=False)),
                ('campaign_percentage', models.IntegerField(blank=True, null=True)),
                ('campaign_price', models.IntegerField(blank=True, null=True)),
                ('total_quantity_of_sell_campaign_product', models.IntegerField(blank=True, null=True)),
                ('total_money_of_sell_campaign_product', models.IntegerField(blank=True, null=True)),
                ('campaign', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.campaign_table')),
                ('category_percentage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.campaign_categories_percentage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.products')),
                ('wishlist', models.ManyToManyField(blank=True, default=None, null=True, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Campaign Product Table',
            },
        ),
        migrations.CreateModel(
            name='campaign_product_attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_Price', models.IntegerField(blank=True, null=True)),
                ('MRP_Price', models.IntegerField(blank=True, null=True)),
                ('Discount_Price', models.IntegerField(blank=True, null=True)),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.attribute_connect_with_product')),
                ('campaign_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.campaign_product_table')),
            ],
            options={
                'verbose_name_plural': 'Campaign Product Attribute',
            },
        ),
        migrations.AddField(
            model_name='campaign_categories_percentage',
            name='Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.category'),
        ),
        migrations.AddField(
            model_name='campaign_categories_percentage',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.campaign_table'),
        ),
        migrations.CreateModel(
            name='Attribute_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribute_value_slag', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Attribute_value_description', models.TextField(blank=True, null=True)),
                ('Attribute_value', models.CharField(max_length=255)),
                ('Attribute_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.attribute')),
            ],
        ),
        migrations.AddField(
            model_name='attribute_connect_with_product',
            name='connect_with_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.products'),
        ),
    ]