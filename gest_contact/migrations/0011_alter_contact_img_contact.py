# Generated by Django 5.0.1 on 2024-01-09 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_contact', '0010_alter_contact_img_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='img_contact',
            field=models.ImageField(blank=True, default='profile/profile.png', upload_to='profile/'),
        ),
    ]
