# Generated by Django 4.2.4 on 2023-10-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0006_joboffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='about',
            field=models.CharField(max_length=200),
        ),
    ]
