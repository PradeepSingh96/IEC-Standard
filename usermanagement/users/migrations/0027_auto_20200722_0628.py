# Generated by Django 3.0.8 on 2020-07-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20200722_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='category',
            field=models.CharField(choices=[('Commercial_tools_with_PLC_hardware_support', 'Commercial tools with PLC hardware support'), ('Open_source_tools', 'Open source tools'), ('Academic_and_research_developments', 'Academic and research developments')], default='Academic and research developments', max_length=200),
        ),
    ]
