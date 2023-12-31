# Generated by Django 4.2.5 on 2023-10-25 07:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0009_alter_category_options_book_available_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]
