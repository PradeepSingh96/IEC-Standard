# Generated by Django 3.0.8 on 2020-07-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20200722_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[('Student_projects', 'Student projects'), ('Test_beds ', 'Testbeds')], default='None', max_length=200),
        ),
    ]