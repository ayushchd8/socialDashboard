# Generated by Django 4.1.6 on 2023-03-04 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_profile_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="password",
        ),
    ]
