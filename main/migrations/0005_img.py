# Generated by Django 4.2.2 on 2023-06-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_booking_duration_customer_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Img",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
