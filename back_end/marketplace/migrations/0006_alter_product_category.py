# Generated by Django 5.0.3 on 2024-03-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0005_pricerate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("UI_KIT", "UI Kit"),
                    ("TEMPLATE", "Template"),
                    ("FRAMER", "Framer"),
                    ("WEBFLOW", "Webflow"),
                    ("BADGE", "Badge"),
                    ("CODED_TEMPLATE", "Coded Templates"),
                ],
                default="UI_KIT",
                max_length=50,
            ),
        ),
    ]
