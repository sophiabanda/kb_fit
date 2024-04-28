# Generated by Django 4.2.11 on 2024-04-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb_fit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionentry',
            name='warmup',
            field=models.ManyToManyField(related_name='warmup_sessions', to='kb_fit.exercise'),
        ),
        migrations.AlterField(
            model_name='sessionentry',
            name='exercise',
            field=models.ManyToManyField(related_name='exercise_sessions', to='kb_fit.exercise'),
        ),
    ]
