# Generated by Django 5.1.5 on 2025-02-10 13:12

import E_Notification.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Notification', '0005_alter_notification_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='order_id',
            field=models.CharField(default=E_Notification.models.Notification.generate_order_id, editable=False, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
