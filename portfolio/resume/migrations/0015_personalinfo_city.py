# Generated by Django 4.2 on 2023-07-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_personalinfo_birth_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
