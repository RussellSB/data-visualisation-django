# Generated by Django 3.2.4 on 2021-06-13 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0002_csv_model_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='model_type',
        ),
    ]
