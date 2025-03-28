# Generated by Django 4.2 on 2024-11-09 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0004_alter_brandusers_password_alter_menuitem_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='admin_dashboard.brandsdetails')),
            ],
            options={
                'db_table': 'Brand_address',
                'unique_together': {('brand', 'address', 'city', 'state', 'postal_code', 'country')},
            },
        ),
    ]
