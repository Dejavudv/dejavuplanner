# Generated by Django 4.2.7 on 2023-11-23 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_remove_cartorder_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='adress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.adress'),
        ),
    ]