# Generated by Django 5.0.3 on 2024-03-26 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxd', '0005_rename_main_calories_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='calories',
            new_name='calorie',
        ),
    ]