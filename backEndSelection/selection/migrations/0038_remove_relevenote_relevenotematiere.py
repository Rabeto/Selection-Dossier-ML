# Generated by Django 2.2.18 on 2021-10-10 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0037_auto_20211010_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relevenote',
            name='releveNoteMatiere',
        ),
    ]