from django.shortcuts import render
from .merch.models import Item

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'item_list.html', context)