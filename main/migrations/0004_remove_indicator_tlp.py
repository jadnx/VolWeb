# Generated by Django 4.2.4 on 2024-03-10 22:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_indicator_name_alter_indicator_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="indicator",
            name="tlp",
        ),
    ]
