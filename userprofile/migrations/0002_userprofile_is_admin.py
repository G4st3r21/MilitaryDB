# Generated by Django 4.1.7 on 2023-02-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]