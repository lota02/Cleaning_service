# Generated by Django 4.2.2 on 2023-07-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_cleaningservice_customer"),
    ]

    operations = [
        migrations.RemoveField(model_name="cleaningservice", name="customer",),
        migrations.AddField(
            model_name="customer",
            name="name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
