# Generated by Django 3.0.5 on 2020-04-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bus",
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
                ("type", models.CharField(max_length=100)),
                ("reg_number", models.CharField(max_length=100)),
                ("number_of_seats", models.IntegerField()),
            ],
        ),
    ]
