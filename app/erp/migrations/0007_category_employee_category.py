# Generated by Django 5.0.4 on 2024-04-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0006_type_employee_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="employee",
            name="category",
            field=models.ManyToManyField(to="erp.category"),
        ),
    ]