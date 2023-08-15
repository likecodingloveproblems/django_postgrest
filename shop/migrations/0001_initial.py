# Generated by Django 4.2.4 on 2023-08-15 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Shop",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("is_archived", models.BooleanField(default=False, verbose_name="is archived?")),
                ("name", models.CharField(max_length=127, verbose_name="name")),
                (
                    "manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="manager",
                    ),
                ),
            ],
            options={
                "verbose_name": "Shop",
                "verbose_name_plural": "Shops",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("is_archived", models.BooleanField(default=False, verbose_name="is archived?")),
                ("name", models.CharField(max_length=127, verbose_name="product")),
                ("description", models.TextField(verbose_name="description")),
                ("price", models.FloatField(verbose_name="price")),
                ("discount", models.FloatField(verbose_name="discount")),
                ("inventory", models.IntegerField(verbose_name="inventory")),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.shop", verbose_name="shop"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
