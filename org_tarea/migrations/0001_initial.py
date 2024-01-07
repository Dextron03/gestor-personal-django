# Generated by Django 5.0.1 on 2024-01-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1500, null=True)),
                ('hour_completion', models.TimeField(blank=True, null=True)),
                ('date_completion', models.DateField(blank=True, null=True)),
            ],
        ),
    ]