# Generated by Django 3.2.6 on 2021-09-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseaseprediction', '0002_alter_prediction_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='result',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
