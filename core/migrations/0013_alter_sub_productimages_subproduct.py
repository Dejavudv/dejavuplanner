# Generated by Django 4.2.4 on 2023-09-27 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_product_sub_product_product_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_productimages',
            name='subproduct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sub_product'),
        ),
    ]
