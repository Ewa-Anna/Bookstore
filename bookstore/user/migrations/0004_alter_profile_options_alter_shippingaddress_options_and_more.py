# Generated by Django 4.2.5 on 2023-10-28 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user", "0003_alter_shippingaddress_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterModelOptions(
            name="shippingaddress",
            options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="profile",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="shippingaddress",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shippingaddress",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="shipping_address",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="profile",
                to="user.shippingaddress",
            ),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shipping_addresses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddIndex(
            model_name="profile",
            index=models.Index(fields=["user"], name="user_profil_user_id_4f95f8_idx"),
        ),
        migrations.AddIndex(
            model_name="shippingaddress",
            index=models.Index(fields=["street"], name="user_shippi_street_3b7f9a_idx"),
        ),
        migrations.AddIndex(
            model_name="shippingaddress",
            index=models.Index(fields=["city"], name="user_shippi_city_44d320_idx"),
        ),
        migrations.AddIndex(
            model_name="shippingaddress",
            index=models.Index(fields=["state"], name="user_shippi_state_ee9528_idx"),
        ),
        migrations.AddIndex(
            model_name="shippingaddress",
            index=models.Index(
                fields=["country"], name="user_shippi_country_23c305_idx"
            ),
        ),
    ]