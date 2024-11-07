# Generated by Django 4.2 on 2024-09-21 23:29

import admin_dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0003_menucategories_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandusers',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.FileField(upload_to=admin_dashboard.models.menuitem_image_upload_path),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='recipe_details',
            field=models.CharField(max_length=500),
        ),
    ]