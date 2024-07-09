from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
def detail(request, pk):
    product = get_object_or_404(Item, pk=pk)
    other = Item.objects.filter(is_sold=False).exclude(pk=pk)[0:2]
    return render(request, 'product/detail.html', {
        'product': product,
        'other': other
    })