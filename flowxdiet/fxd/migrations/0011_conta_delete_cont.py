# Generated by Django 5.0.3 on 2024-04-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxd', '0010_cont_delete_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('contactno', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('postalcode', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='cont',
        ),
    ]
