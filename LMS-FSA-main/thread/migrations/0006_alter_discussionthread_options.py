# Generated by Django 5.0.9 on 2024-09-20 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("thread", "0005_threadcomments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="discussionthread",
            options={"ordering": ["-updated"]},
        ),
    ]
