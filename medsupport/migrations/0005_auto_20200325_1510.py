# Generated by Django 3.0.4 on 2020-03-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0004_auto_20200325_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='attached_files',
            field=models.FileField(blank=True, null=True, upload_to='articles/attached_files', verbose_name='Прикріплені файли'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='attached_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/image_files', verbose_name='Прикріплене зображення'),
        ),
    ]
