# Generated by Django 4.2.1 on 2023-05-09 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0003_alter_address_number_alter_address_zip_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="number",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="zip_code",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
