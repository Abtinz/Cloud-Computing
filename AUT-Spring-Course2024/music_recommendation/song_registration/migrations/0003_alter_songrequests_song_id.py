# Generated by Django 5.0.1 on 2024-03-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("song_registration", "0002_songrequests_song_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="songrequests",
            name="song_id",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
