# Generated by Django 4.2.4 on 2023-10-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_product_old_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=3, default='200,000', max_digits=999999999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default='100,000', max_digits=999999999999999999),
        ),
    ]
