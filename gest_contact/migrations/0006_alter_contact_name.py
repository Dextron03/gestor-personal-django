# Generated by Django 5.0.1 on 2024-01-08 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_contact', '0005_contact_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(error_messages={'required': 'Mi mensaje personalizado'}, max_length=50),
        ),
    ]