# Generated by Django 3.1.2 on 2020-10-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20201023_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=0),
        ),
    ]
