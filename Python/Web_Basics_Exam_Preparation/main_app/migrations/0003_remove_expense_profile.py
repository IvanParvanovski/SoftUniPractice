# Generated by Django 3.1.2 on 2020-10-30 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_expense_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='profile',
        ),
    ]