# Generated by Django 4.2 on 2023-07-15 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_personalinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='degree',
        ),
    ]