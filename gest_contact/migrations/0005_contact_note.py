# Generated by Django 5.0.1 on 2024-01-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_contact', '0004_alter_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
