# Generated by Django 4.2.11 on 2024-04-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb_fit', '0005_alter_exercise_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='sets',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]