# Generated by Django 3.0.4 on 2020-10-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crisis", "0009_auto_20200412_1719")]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="type",
            field=models.CharField(
                choices=[("G", "Grocery"), ("M", "Medicine"), ("O", "Other")],
                default="O",
                max_length=2,
            ),
        )
    ]
