# Generated by Django 5.0.3 on 2024-03-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0006_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="templateformat",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
