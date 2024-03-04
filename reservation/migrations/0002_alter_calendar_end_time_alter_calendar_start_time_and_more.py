# Generated by Django 4.2.10 on 2024-03-04 13:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendar",
            name="end_time",
            field=models.TimeField(verbose_name="end time"),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="start_time",
            field=models.TimeField(verbose_name="start time"),
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=False, verbose_name="status of room"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "calendar_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="room_calendar_id",
                        to="reservation.calendar",
                        verbose_name="choose day and time",
                    ),
                ),
            ],
        ),
    ]