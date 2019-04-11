# Generated by Django 2.0.7 on 2019-04-11 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8, unique=True, verbose_name='DNI')),
                ('DNIUpline', models.IntegerField(verbose_name='DNIUpline')),
                ('tipo', models.CharField(blank=True, choices=[('APRENDIZ', 'Aprendiz'), ('MENTOR', 'Mentor')], max_length=10, null=True, verbose_name='Tipo')),
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentores', to='mentor.Mentor')),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentores',
            },
        ),
        migrations.CreateModel(
            name='Mentoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha y hora')),
                ('DNI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentoria', to='mentor.Mentor')),
            ],
            options={
                'verbose_name': 'Mentoria',
                'verbose_name_plural': 'Mentorias',
            },
        ),
    ]
