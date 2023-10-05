# Generated by Django 4.2.4 on 2023-10-02 18:52

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_productreview_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=30, prefix='', unique=True),
        ),
    ]