# Generated by Django 4.2 on 2024-09-08 17:21

import admin_dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0002_alter_brandsdetails_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('order', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.brandsdetails')),
            ],
            options={
                'db_table': 'Menu_categories',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('recipe_details', models.CharField(max_length=125)),
                ('price', models.FloatField()),
                ('image', models.FileField(upload_to='', verbose_name=admin_dashboard.models.menuitem_image_upload_path)),
                ('order', models.IntegerField()),
                ('popular', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.menucategories')),
            ],
            options={
                'db_table': 'Menu_items',
            },
        ),
    ]
