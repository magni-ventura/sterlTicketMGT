# Generated by Django 5.0.4 on 2024-04-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticket",
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
                ("ticket_id", models.CharField(max_length=15, unique=True)),
                ("ticket_title", models.CharField(max_length=100)),
                ("ticket_description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Active", "Active"),
                            ("Pending", "Pending"),
                            ("Resolved", "Resolved"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("is_resolved", models.BooleanField(default=False)),
                (
                    "severity",
                    models.CharField(
                        choices=[("A", "A"), ("B", "B")], default="B", max_length=5
                    ),
                ),
                ("is_assigned_to_engineer", models.BooleanField(default=False)),
                ("resolution_steps", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
