# Generated by Django 3.0.8 on 2020-07-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200721_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='tools/'),
        ),
    ]
