# Generated by Django 4.2.17 on 2025-02-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj_home', '0012_user_avatar_user_birth_date_user_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
