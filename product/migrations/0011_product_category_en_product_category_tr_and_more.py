# Generated by Django 4.1.2 on 2022-10-23 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_tr',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_tr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_tr',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_en',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_tr',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]