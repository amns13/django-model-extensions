# Generated by Django 4.0.6 on 2022-07-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreatedUpdatedTimestampTestModel",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created timestamp"
                    ),
                ),
                (
                    "last_updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="last update timestamp"
                    ),
                ),
            ],
            options={
                "get_latest_by": "last_updated_at",
                "abstract": False,
            },
        ),
    ]
