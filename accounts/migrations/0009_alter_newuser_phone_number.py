# Generated by Django 4.2.10 on 2024-03-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_remove_otpcode_phone_number_newuser_phone_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="phone_number",
            field=models.CharField(verbose_name="phone number"),
        ),
    ]