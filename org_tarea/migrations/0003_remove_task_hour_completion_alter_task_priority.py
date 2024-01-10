# Generated by Django 5.0.1 on 2024-01-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_tarea', '0002_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='hour_completion',
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveSmallIntegerField(default=1, help_text='A mayor número, mayor prioridad.'),
        ),
    ]