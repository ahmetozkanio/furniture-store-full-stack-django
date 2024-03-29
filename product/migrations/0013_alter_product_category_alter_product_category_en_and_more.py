# Generated by Django 4.1.2 on 2022-10-23 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_en',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_tr',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category'),
        ),
    ]
