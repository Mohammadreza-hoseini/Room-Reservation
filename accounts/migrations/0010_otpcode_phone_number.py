# Generated by Django 4.2.10 on 2024-03-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_newuser_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="otpcode",
            name="phone_number",
            field=models.CharField(default="", verbose_name="phone number"),
            preserve_default=False,
        ),
    ]