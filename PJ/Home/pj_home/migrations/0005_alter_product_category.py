# Generated by Django 5.1.5 on 2025-02-12 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj_home', '0004_remove_orderdetail_stock_orderdetail_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('kim_cuong', 'Kim Cương'), ('vang', 'Vàng'), ('bac', 'Bạc')], max_length=255),
        ),
    ]
