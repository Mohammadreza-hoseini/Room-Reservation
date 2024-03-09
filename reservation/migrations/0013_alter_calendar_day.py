# Generated by Django 4.2.10 on 2024-03-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0012_alter_room_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendar",
            name="day",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "saturday"),
                    (1, "sunday"),
                    (2, "monday"),
                    (3, "tuesday"),
                    (4, "wednesday"),
                    (5, "thursday"),
                    (6, "friday"),
                ],
                default=0,
                verbose_name="select day",
            ),
        ),
    ]
