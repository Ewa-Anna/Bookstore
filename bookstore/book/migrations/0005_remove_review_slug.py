# Generated by Django 4.2.5 on 2023-09-20 15:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0004_review_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="slug",
        ),
    ]