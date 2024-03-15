# Generated by Django 5.0.1 on 2024-03-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Request",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("done", "Done"),
                            ("failure", "Failure"),
                            ("pending", "Pending"),
                            ("ready", "Ready"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                ("song_id", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
