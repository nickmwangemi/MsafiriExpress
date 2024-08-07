# Generated by Django 3.0.5 on 2020-04-29 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("buses", "0002_auto_20200429_1119"),
        ("travel_routes", "0004_auto_20200429_1202"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("number_of_tickets", models.IntegerField(default=1)),
                ("date_of_booking", models.DateTimeField(auto_now_add=True)),
                (
                    "bus_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="buses.Bus"
                    ),
                ),
                (
                    "customer_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "route",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="travel_routes.TravelRoute",
                    ),
                ),
            ],
        ),
    ]
