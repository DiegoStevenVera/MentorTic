# Generated by Django 2.0.7 on 2019-04-12 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0005_auto_20190412_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='mentor',
        ),
        migrations.AddField(
            model_name='mentor',
            name='mentorPadre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Mentores', to='mentor.Mentor'),
        ),
    ]
