# Generated by Django 2.2.18 on 2021-10-09 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0033_compte_compteparcours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='dossierNumInscription',
            field=models.CharField(max_length=8),
        ),
    ]
