# Generated by Django 4.2.2 on 2023-06-22 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cleaningservice", old_name="user", new_name="name",
        ),
    ]
