from model_bakery import baker

from shop.models import Product, Shop


def run():
    shops = baker.make(Shop, _quantity=1000, _bulk_create=True)
    for shop in shops:
        baker.make(Product, _quantity=200, _bulk_create=True, shop=shop)
