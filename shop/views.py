from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Product, Shop
from shop.permissions import IsShopManager
from shop.serializers import ProductSerializer


class ShopProductsView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsShopManager,
    )
    serializer_class = ProductSerializer

    def get(self, request, shop_id):
        shop = self.get_shop(shop_id)
        products = self.get_products(shop)
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)

    @staticmethod
    def get_shop(shop_id):
        return get_object_or_404(Shop, id=shop_id)

    @staticmethod
    def get_products(shop):
        return Product.objects.for_shop(shop).available()
