# Generated by Django 3.0.4 on 2020-03-30 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0004_auto_20200330_1042"),
        ("crisis", "0002_auto_20200329_1031"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="assignee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="assigned_request",
                to="management.Participant",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_request",
                to="management.Participant",
            ),
        ),
        migrations.AlterField(
            model_name="requestassignment",
            name="assignee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignment",
                to="management.Participant",
            ),
        ),
    ]
