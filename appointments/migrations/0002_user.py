# Generated by Django 2.0 on 2024-04-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('medicalhistory', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
    ]
