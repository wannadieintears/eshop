# Generated by Django 4.2.5 on 2023-10-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bboard_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bboard',
            name='name',
            field=models.SlugField(),
        ),
    ]
