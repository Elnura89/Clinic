# Generated by Django 4.2.7 on 2023-12-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('date', models.TimeField()),
                ('time', models.TimeField()),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
    ]
