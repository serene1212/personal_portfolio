# Generated by Django 5.1 on 2024-08-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_jobexperience_options_alter_education_end_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="technologies",
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
