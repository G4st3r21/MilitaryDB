# Generated by Django 4.1.5 on 2023-01-28 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MilitaryMuseum', '0008_rename_picture_videos_video_combatants_patronymic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.AlterField(
            model_name='combatants',
            name='native_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MilitaryMuseum.cities', verbose_name='Родной город'),
        ),
    ]
