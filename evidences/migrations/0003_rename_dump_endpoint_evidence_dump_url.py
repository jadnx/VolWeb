# Generated by Django 4.2.11 on 2024-05-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evidences', '0002_evidence_dump_access_key_evidence_dump_access_key_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidence',
            old_name='dump_endpoint',
            new_name='dump_url',
        ),
    ]