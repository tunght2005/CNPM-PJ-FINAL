# Generated by Django 5.1.4 on 2024-12-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('customer_email', models.EmailField(max_length=254)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
