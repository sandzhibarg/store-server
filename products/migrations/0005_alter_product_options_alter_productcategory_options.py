# Generated by Django 4.2.1 on 2023-05-17 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_basket_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'категории'},
        ),
    ]