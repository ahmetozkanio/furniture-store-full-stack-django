# Generated by Django 4.1.2 on 2022-10-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_image_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]