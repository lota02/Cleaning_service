# Generated by Django 4.2.2 on 2023-07-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("main", "0011_remove_review_customer_remove_review_service_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(name="customer", managers=[],),
        migrations.AlterField(
            model_name="customer",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this customer belongs to.",
                related_name="customer_groups",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this customer.",
                related_name="customer_user_permissions",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]