# Generated by Django 4.2 on 2023-07-16 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_rename_icon_name_navbar_section_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='birth_year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
