# Generated by Django 3.2.4 on 2021-06-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='model_type',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
