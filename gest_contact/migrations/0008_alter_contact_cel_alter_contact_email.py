# Generated by Django 5.0.1 on 2024-01-08 03:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_contact', '0007_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cel',
            field=models.CharField(max_length=12, validators=[django.core.validators.MaxLengthValidator(limit_value=12, message='<div class="alert alert-warning alert-dismissible fade show" role="alert"> Tu numero de telefono no es valido. <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='<div class="alert alert-warning alert-dismissible fade show" role="alert"> Ingresa una dirección de correo electrónico válida <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')]),
        ),
    ]
