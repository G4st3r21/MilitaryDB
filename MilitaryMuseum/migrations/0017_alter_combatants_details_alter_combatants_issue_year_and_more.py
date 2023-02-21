# Generated by Django 4.1.5 on 2023-02-14 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MilitaryMuseum', '0016_alter_combatants_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combatants',
            name='details',
            field=models.TextField(blank=True, null=True, verbose_name='Подробности'),
        ),
        migrations.AlterField(
            model_name='combatants',
            name='issue_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='combatants',
            name='place_of_birth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MilitaryMuseum.places', verbose_name='Место рождения'),
        ),
    ]
