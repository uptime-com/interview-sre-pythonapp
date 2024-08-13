from django.db import models


class ShoppingList(models.Model):
    item = models.CharField(max_length=50)
