# Generated by Django 4.1.5 on 2023-01-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MilitaryMuseum', '0002_alter_combatants_options_alter_pictures_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='combatants',
            name='native_city',
            field=models.CharField(max_length=50, null=True, verbose_name='Родной город'),
        ),
        migrations.AlterField(
            model_name='combatants',
            name='details',
            field=models.TextField(null=True, verbose_name='Подробности'),
        ),
    ]
