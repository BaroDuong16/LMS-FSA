# Generated by Django 5.0.9 on 2024-09-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration_member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
