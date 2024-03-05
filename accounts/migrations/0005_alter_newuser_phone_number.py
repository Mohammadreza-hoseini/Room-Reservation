# Generated by Django 4.2.10 on 2024-03-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_newuser_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="phone_number",
            field=models.CharField(
                blank=True, null=True, unique=True, verbose_name="phone number"
            ),
        ),
    ]
