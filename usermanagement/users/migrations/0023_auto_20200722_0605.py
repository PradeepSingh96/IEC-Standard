# Generated by Django 3.0.8 on 2020-07-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200722_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[('Student_projects', 'Student projects'), ('Test_beds ', 'Testbeds')], default='Student projects', max_length=200),
        ),
    ]
