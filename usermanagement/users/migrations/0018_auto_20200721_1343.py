# Generated by Django 3.0.8 on 2020-07-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200721_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='color',
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(choices=[('Student_projects', 'Student projects'), ('Testbeds ', 'Testbeds')], default='Student projects', max_length=200),
        ),
        migrations.AlterField(
            model_name='tools',
            name='description',
            field=models.CharField(choices=[('Commercial_tools_with_PLC_hardware_support', 'Commercial tools with PLC hardware support'), ('Open_source_tools ', 'Open source tools'), ('Academic_and_research_developments ', 'Academic and research developments')], default='Academic and research developments', max_length=200),
        ),
    ]
