# Generated by Django 4.1.6 on 2023-03-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_profile_email_profile_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
