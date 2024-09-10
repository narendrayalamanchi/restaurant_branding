# Generated by Django 5.1.1 on 2024-09-08 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('logo', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'Brand_details',
            },
        ),
        migrations.CreateModel(
            name='BrandUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.brandsdetails')),
            ],
            options={
                'db_table': 'Brand_users',
            },
        ),
    ]
