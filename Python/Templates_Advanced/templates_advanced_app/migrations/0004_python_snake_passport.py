# Generated by Django 3.1.3 on 2020-11-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_advanced_app', '0003_auto_20201114_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='python',
            name='snake_passport',
            field=models.FileField(default='', upload_to='snake_documents'),
            preserve_default=False,
        ),
    ]