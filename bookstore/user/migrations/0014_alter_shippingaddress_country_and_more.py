# Generated by Django 4.2.5 on 2024-01-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0013_alter_shippingaddress_postal_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingaddress",
            name="country",
            field=models.CharField(max_length=100, verbose_name="Country"),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="state",
            field=models.CharField(max_length=100, verbose_name="State"),
        ),
    ]
