# Generated by Django 4.2.2 on 2023-07-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_booking_name_alter_booking_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking", name="time", field=models.TimeField(default="20:50"),
        ),
    ]