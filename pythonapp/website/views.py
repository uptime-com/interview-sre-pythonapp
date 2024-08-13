from django.shortcuts import render
from .models import ShoppingList

def homepage(request):
    ctx = {
        "shopping_list": [sl.item for sl in ShoppingList.objects.all()],
    }
    return render(request, "website/homepage.html", ctx)
