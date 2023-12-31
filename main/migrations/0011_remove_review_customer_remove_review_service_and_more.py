# Generated by Django 4.2.2 on 2023-07-06 14:54

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("main", "0010_delete_customuser"),
    ]

    operations = [
        migrations.RemoveField(model_name="review", name="customer",),
        migrations.RemoveField(model_name="review", name="service",),
        migrations.AlterModelOptions(
            name="customer",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelManagers(
            name="customer",
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.RenameField(
            model_name="booking", old_name="service", new_name="cleaning_service",
        ),
        migrations.RemoveField(model_name="booking", name="date_time",),
        migrations.RemoveField(model_name="booking", name="status",),
        migrations.RemoveField(model_name="customer", name="name",),
        migrations.RemoveField(model_name="customer", name="user",),
        migrations.AddField(
            model_name="booking",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="booking",
            name="time",
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AddField(
            model_name="customer",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this customer belongs to.",
                related_name="customer_set",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="password",
            field=models.CharField(default=1, max_length=128, verbose_name="password"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this customer.",
                related_name="customer_set",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="username",
            field=models.CharField(
                default=1,
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="booking", name="duration", field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone_number",
            field=models.CharField(max_length=15),
        ),
        migrations.DeleteModel(name="Payment",),
        migrations.DeleteModel(name="Review",),
    ]
