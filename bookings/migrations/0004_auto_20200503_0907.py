# Generated by Django 3.0.5 on 2020-05-03 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0003_booking_amount_paid"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"verbose_name_plural": "Bookings"},
        ),
    ]
