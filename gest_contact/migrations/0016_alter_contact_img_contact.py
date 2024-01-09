# Generated by Django 5.0.1 on 2024-01-09 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_contact', '0015_alter_contact_img_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='img_contact',
            field=models.ImageField(blank=True, null=True, upload_to='profile/profile.png', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'], message='<div class="alert alert-warning alert-dismissible fade show" role="alert"> Solo acepta archivos png y jpg <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')]),
        ),
    ]
