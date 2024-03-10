# Generated by Django 4.2.10 on 2024-03-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_comment_room"),
    ]

    operations = [
        migrations.AddField(
            model_name="newuser",
            name="otp_expire",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="otp expire time"
            ),
        ),
    ]
