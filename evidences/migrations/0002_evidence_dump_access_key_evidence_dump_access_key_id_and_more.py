# Generated by Django 4.2.11 on 2024-04-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='dump_access_key',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dump_access_key_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dump_endpoint',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evidence',
            name='dump_source',
            field=models.CharField(choices=[('AWS', 'AWS'), ('MINIO', 'MINIO')], max_length=10, null=True),
        ),
    ]
