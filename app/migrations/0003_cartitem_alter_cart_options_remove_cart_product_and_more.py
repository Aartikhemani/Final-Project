# Generated by Django 4.1 on 2022-08-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_tags_tag_alter_category_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CartItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name="cart",
            options={},
        ),
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="quantity",
        ),
        migrations.AddField(
            model_name="cart",
            name="items",
            field=models.ManyToManyField(through="app.CartItem", to="app.product"),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.cart"
            ),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.product"
            ),
        ),
    ]