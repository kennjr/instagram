# Generated by Django 4.0.3 on 2022-04-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_localuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
