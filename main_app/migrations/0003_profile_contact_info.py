# Generated by Django 4.1.1 on 2023-01-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_alter_preference_interest"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="contact_info",
            field=models.CharField(default="test", max_length=250),
            preserve_default=False,
        ),
    ]