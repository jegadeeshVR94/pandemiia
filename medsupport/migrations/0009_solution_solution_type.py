# Generated by Django 3.0.4 on 2020-04-28 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0008_auto_20200428_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medsupport.SolutionType', verbose_name='Тип рішення'),
        ),
    ]
