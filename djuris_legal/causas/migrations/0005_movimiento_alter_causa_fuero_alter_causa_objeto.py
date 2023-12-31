# Generated by Django 4.2.6 on 2023-11-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("causas", "0004_alter_causa_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movimiento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("fecha", models.DateField()),
                (
                    "tipo",
                    models.CharField(
                        choices=[("inicio", "Inicio"), ("mero tramite", "Tramite"), ("recurso", "Recurso")],
                        default=None,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="causa",
            name="fuero",
            field=models.CharField(choices=[("Fam", "Familia"), ("Civ", "Civil"), ("Pen", "Penal")], default=None),
        ),
        migrations.AlterField(
            model_name="causa",
            name="objeto",
            field=models.CharField(
                choices=[
                    ("AL", "Alimentos"),
                    ("CP", "Cuidado Personal"),
                    ("DV", "Divorcio Vincular"),
                    ("Su", "Sucesion"),
                ],
                default=None,
            ),
        ),
    ]
