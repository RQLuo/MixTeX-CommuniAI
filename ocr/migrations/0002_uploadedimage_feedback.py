# Generated by Django 4.0.6 on 2024-02-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
