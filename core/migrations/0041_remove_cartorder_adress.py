# Generated by Django 4.2.7 on 2023-11-23 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_cartorder_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='adress',
        ),
    ]
