# Generated by Django 3.0.4 on 2020-05-01 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0009_auto_20200501_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalneed',
            name='units',
        ),
        migrations.AddField(
            model_name='solutiontype',
            name='units',
            field=models.CharField(choices=[('pieces', 'шт'), ('packs', 'уп'), ('vials', 'фл')], default='pieces', max_length=255, verbose_name='Одиниці вимірювання'),
        ),
        migrations.AlterField(
            model_name='hospitalneed',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needs', to='medsupport.Hospital', verbose_name='Лікарня'),
        ),
        migrations.AlterField(
            model_name='hospitalneed',
            name='solution_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_needs', to='medsupport.SolutionType', verbose_name='Тип рішення'),
        ),
    ]