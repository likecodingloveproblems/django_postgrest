from django.urls import path

from shop.views import ShopProductsView

app_name = "users"
urlpatterns = [
    path("<int:shop_id>/products/", view=ShopProductsView.as_view(), name="shop-products"),
]
