# Generated by Django 2.2.18 on 2021-09-25 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0031_auto_20210925_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compte',
            name='compteParcours',
        ),
    ]
