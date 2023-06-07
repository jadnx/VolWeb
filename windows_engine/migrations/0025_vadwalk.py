# Generated by Django 3.2.18 on 2023-04-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investigations', '0001_initial'),
        ('windows_engine', '0024_auto_20230423_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='VadWalk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('End', models.TextField(null=True)),
                ('Left', models.TextField(null=True)),
                ('Offset', models.TextField(null=True)),
                ('PID', models.BigIntegerField()),
                ('Parent', models.TextField(null=True)),
                ('Process', models.TextField(null=True)),
                ('Right', models.TextField(null=True)),
                ('Start', models.TextField(null=True)),
                ('VTag', models.TextField(null=True)),
                ('Tag', models.CharField(choices=[('Evidence', 'Evidence'), ('Suspicious', 'Suspicious')], max_length=11, null=True)),
                ('investigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='windows_vadwalk_investigation', to='investigations.uploadinvestigation')),
            ],
        ),
    ]