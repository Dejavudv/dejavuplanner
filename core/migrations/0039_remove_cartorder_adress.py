# Generated by Django 4.2.7 on 2023-11-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_cartorder_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='adress',
        ),
    ]
