# Generated by Django 2.0.7 on 2019-04-25 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0003_auto_20190413_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('DNI', models.CharField(blank=True, max_length=8, null=True, unique=True, verbose_name='DNI')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='correo electronico')),
                ('first_name', models.CharField(max_length=100, verbose_name='nombres')),
                ('last_name', models.CharField(max_length=100, verbose_name='apellidos')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user', verbose_name='foto')),
                ('gender', models.CharField(blank=True, choices=[('HOMBRE', 'hombre'), ('MUJER', 'mujer')], max_length=20, null=True, verbose_name='genero')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='celular')),
            ],
            options={
                'verbose_name': 'Representante',
                'verbose_name_plural': 'Representantes',
            },
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='celular',
        ),
        migrations.AddField(
            model_name='entidad',
            name='esFicticia',
            field=models.BooleanField(default=False, verbose_name='Es ficticia?'),
        ),
        migrations.AddField(
            model_name='entidad',
            name='representante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entidad', to='entidad.Representante'),
        ),
    ]
