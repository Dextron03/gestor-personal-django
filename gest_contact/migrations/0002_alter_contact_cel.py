# Generated by Django 5.0.1 on 2024-01-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cel',
            field=models.CharField(max_length=10),
        ),
    ]
