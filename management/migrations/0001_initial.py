# Generated by Django 3.0.4 on 2020-03-29 10:31

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("crisis", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ability",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(max_length=30, verbose_name="Name of ability"),
                ),
                (
                    "verb",
                    models.CharField(
                        choices=[
                            ("F", "Fetch"),
                            ("P", "Provide"),
                            ("T", "Transport"),
                            ("N", "Notify"),
                        ],
                        default="F",
                        max_length=3,
                        verbose_name="Action on the title, (eg, GET)",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("HL", "Helper"),
                            ("AF", "Affected"),
                            ("AU", "Authorities"),
                            ("TP", "Third Parties"),
                        ],
                        max_length=2,
                    ),
                ),
                ("first_line_of_address", models.CharField(max_length=255)),
                ("second_line_of_address", models.CharField(max_length=255)),
                ("country", django_countries.fields.CountryField(max_length=2)),
                (
                    "place_id",
                    models.CharField(
                        max_length=150, verbose_name="Place id from Google"
                    ),
                ),
                (
                    "position",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                (
                    "post_code",
                    models.CharField(max_length=10, verbose_name="Postal code"),
                ),
                ("city", models.CharField(max_length=40, verbose_name="City")),
                (
                    "phone",
                    phone_field.models.PhoneField(
                        blank=True, help_text="Contact phone number", max_length=31
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "crisis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="crisis.Crisis",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
