# Generated by Django 5.0.1 on 2024-03-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("song_registration", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="songrequests",
            name="song_url",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
