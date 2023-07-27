# Generated by Django 4.2 on 2023-07-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_personalinfo_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]