# Generated by Django 4.2.4 on 2023-08-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0002_cart_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="cartproducts",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
