# Generated by Django 4.2.5 on 2023-10-08 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bboard',
            name='date',
        ),
    ]