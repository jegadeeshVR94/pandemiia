# Generated by Django 3.0.4 on 2020-04-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0006_auto_20200420_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='source',
            field=models.URLField(blank=True, verbose_name='Джерело'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='region',
            field=models.IntegerField(choices=[(1, 'Вінницька область'), (2, 'Волинська область'), (3, 'Дніпропетровська область'), (4, 'Донецька область'), (5, 'Житомирська область'), (6, 'Закарпатська область'), (7, 'Запорізька область'), (8, 'Івано-Франківська область'), (9, 'Київська область'), (10, 'Кіровоградська область'), (11, 'Луганська область'), (12, 'Львівська область'), (13, 'Миколаївська область'), (14, 'Одеська область'), (15, 'Полтавська область'), (16, 'Рівненська область'), (17, 'Сумська область'), (18, 'Тернопільська область'), (19, 'Харківська область'), (20, 'Херсонська область'), (21, 'Хмельницька область'), (22, 'Черкаська область'), (23, 'Чернівецька область'), (24, 'Чернігівська область'), (25, 'м. Київ'), (26, 'АР Крим')], verbose_name='Область'),
        ),
    ]
