# Generated by Django 4.2.4 on 2023-08-13 20:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="место"
                    ),
                ),
                (
                    "activity",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="действие"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="награда"
                    ),
                ),
                (
                    "of_publicity",
                    models.BooleanField(default=False, verbose_name="публичность"),
                ),
                (
                    "time",
                    models.TimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Время выполнения привычки",
                    ),
                ),
                (
                    "good_habit_sign",
                    models.BooleanField(
                        default=False, verbose_name="признак приятной привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.IntegerField(default=1, verbose_name="периодичность"),
                ),
                (
                    "execution_time",
                    models.TimeField(
                        default="00:02", verbose_name="время на выполнение"
                    ),
                ),
                (
                    "relted_habbit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Atomic_Habits.habits",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
                "ordering": ["time"],
            },
        ),
    ]
