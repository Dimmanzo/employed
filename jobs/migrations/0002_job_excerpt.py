# Generated by Django 4.2.16 on 2024-09-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
