# Generated by Django 3.1.2 on 2020-10-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201031_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Cat', 'cat'), ('Dog', 'dog'), ('Parrot', 'parrot')], default='', max_length=6),
        ),
    ]