# Generated by Django 4.1.5 on 2023-02-03 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MilitaryMuseum', '0010_places_remove_combatants_native_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BGPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/backgrounds', verbose_name='Фоновое изображение')),
                ('is_main_picture', models.BooleanField(default=True, verbose_name='Использовать как основную')),
            ],
            options={
                'verbose_name': 'Фоновое изображение сайта',
                'verbose_name_plural': 'Фоновые изображения сайта',
            },
        ),
        migrations.AlterField(
            model_name='combatants',
            name='place_of_birth',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MilitaryMuseum.places', verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='picture',
            field=models.ImageField(upload_to='images/combatants/', verbose_name='Изображение'),
        ),
    ]
