# Generated by Django 4.2.5 on 2023-10-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0010_alter_bboard_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bboard',
            name='date',
        ),
    ]
