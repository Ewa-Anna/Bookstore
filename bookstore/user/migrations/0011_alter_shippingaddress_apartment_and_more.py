# Generated by Django 4.2.5 on 2023-11-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0010_alter_shippingaddress_main"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingaddress",
            name="apartment",
            field=models.CharField(max_length=30, verbose_name="Apartment Number"),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="city",
            field=models.CharField(max_length=100, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="postal_code",
            field=models.CharField(max_length=10, verbose_name="Postal Code"),
        ),
        migrations.AlterField(
            model_name="shippingaddress",
            name="street",
            field=models.CharField(max_length=255, verbose_name="Street Address"),
        ),
    ]
