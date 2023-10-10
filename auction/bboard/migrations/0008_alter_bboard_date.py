# Generated by Django 4.2.5 on 2023-10-10 18:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_bboard_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bboard',
            name='date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
