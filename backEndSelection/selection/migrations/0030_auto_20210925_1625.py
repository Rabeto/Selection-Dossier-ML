# Generated by Django 2.2.18 on 2021-09-25 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0029_auto_20210925_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='compteParcours',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='selection.Parcours'),
        ),
    ]
