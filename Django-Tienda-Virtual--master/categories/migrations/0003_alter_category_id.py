# Generated by Django 4.2.4 on 2023-08-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_category_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
