# Generated by Django 3.1.2 on 2020-10-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]