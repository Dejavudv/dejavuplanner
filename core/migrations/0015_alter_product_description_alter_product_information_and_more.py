# Generated by Django 4.2.4 on 2023-10-01 07:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_sub_productimages_subproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='this is the product', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='this is the information part', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='more_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='this is more product', null=True),
        ),
    ]
