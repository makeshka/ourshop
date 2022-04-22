from decimal import Decimal

from django.conf import settings

from store.models import Product


class Wishlist():
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if settings.WISHLIST_SESSION_ID not in request.session:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}
        self.wishlist = wishlist

    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.wishlist:
            self.wishlist[product_id]['qty'] = qty
        else:
            self.wishlist[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        product_ids = self.wishlist.keys()
        products = Product.products.filter(id__in=product_ids)
        wishlist = self.wishlist.copy()

        for product in products:
            wishlist[str(product.id)]['product'] = product

    def delete(self, product):
        product_id = str(product)

        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.save()

    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True