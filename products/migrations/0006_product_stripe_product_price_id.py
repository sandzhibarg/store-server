# Generated by Django 4.2.1 on 2023-05-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_options_alter_productcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
