# Generated by Django 2.0.7 on 2019-04-11 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentoria',
            old_name='DNI',
            new_name='mentor',
        ),
    ]
