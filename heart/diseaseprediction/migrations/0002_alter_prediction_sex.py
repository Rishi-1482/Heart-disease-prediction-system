# Generated by Django 3.2.6 on 2021-09-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseaseprediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='sex',
            field=models.PositiveIntegerField(),
        ),
    ]