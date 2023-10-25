# Generated by Django 4.2.5 on 2023-10-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0010_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
            ),
        ),
    ]