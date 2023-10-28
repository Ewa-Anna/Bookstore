# Generated by Django 4.2.5 on 2023-10-27 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("book", "0013_vote"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="review",
            name="book_review_name_969e5b_idx",
        ),
        migrations.RemoveField(
            model_name="review",
            name="email",
        ),
        migrations.RemoveField(
            model_name="review",
            name="name",
        ),
        migrations.AddField(
            model_name="review",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddIndex(
            model_name="review",
            index=models.Index(fields=["user"], name="book_review_user_id_9c8336_idx"),
        ),
    ]