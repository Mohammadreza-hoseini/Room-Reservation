# Generated by Django 4.2.10 on 2024-03-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="otp",
            field=models.SmallIntegerField(default=0, verbose_name="otp code"),
        ),
        migrations.AlterField(
            model_name="newuser",
            name="phone_number",
            field=models.SmallIntegerField(
                default=0, unique=True, verbose_name="phone number"
            ),
        ),
    ]
