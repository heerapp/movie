# Generated by Django 3.1.4 on 2022-03-03 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220303_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
    ]