# Generated by Django 4.2 on 2023-07-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_personalinfo_birthday_personalinfo_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
