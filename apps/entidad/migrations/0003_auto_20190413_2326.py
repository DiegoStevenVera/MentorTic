# Generated by Django 2.0.7 on 2019-04-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0002_auto_20190412_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='celular',
            field=models.CharField(max_length=12, verbose_name='Celular'),
        ),
    ]
