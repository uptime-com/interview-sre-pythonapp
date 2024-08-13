# Generated by Django 5.1 on 2024-08-13 13:30

from django.db import migrations


def populate_shopping_list(apps, schema_editor):
    ShoppingList = apps.get_model("website", "ShoppingList")
    ShoppingList.objects.create(item="Bananas")
    ShoppingList.objects.create(item="Apples")
    ShoppingList.objects.create(item="Milk")
    ShoppingList.objects.create(item="Yoghurt")


def depopulate_shopping_list(apps, schema_editor):
    ShoppingList = apps.get_model("website", "ShoppingList")
    ShoppingList.objects.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_shopping_list, depopulate_shopping_list),
    ]
