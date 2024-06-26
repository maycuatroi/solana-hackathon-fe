# Generated by Django 5.0.3 on 2024-03-23 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0007_alter_templateformat_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SaleHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("price_unit", models.CharField(default="sol", max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchased_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_histories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale_histories",
                        to="marketplace.product",
                    ),
                ),
            ],
        ),
    ]
