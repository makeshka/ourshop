from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .wishlist import Wishlist


def wishlist_page(request):
    wishlist = Wishlist(request)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})


def wishlist_add(request):
    wishlist = Wishlist(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        wishlist.add(product=product)


def wishlist_delete(request):
    wishlist = Wishlist(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        wishlist.delete(product=product_id)
