# Generated by Django 3.0.4 on 2020-03-30 10:42

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("management", "0003_auto_20200329_1041")]

    operations = [
        migrations.AlterField(
            model_name="participant",
            name="position",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, geography=True, null=True, srid=4326
            ),
        )
    ]
