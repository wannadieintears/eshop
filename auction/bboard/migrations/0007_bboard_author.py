# Generated by Django 4.2.5 on 2023-10-08 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('bboard', '0006_alter_bboard_description_alter_bboard_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bboard',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]