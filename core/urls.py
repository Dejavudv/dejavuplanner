from django.urls import path
from core.views import *
# index, category_list_view, product_list_view,category_product_list_view, custom_product_list
# from core import *


app_name = "core"
urlpatterns = [
    path("", index, name = "index"),
    path("products/", product_list_view, name = "product-list"),
    path("product/<pid>/", product_detail_view, name = "product-detail"),
    path("category/", category_list_view, name = "category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    path("custom/", custom_product_list, name="custom"),
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax_add_review"),
    path("search/", search_view, name="search"),
    path("filter-products/", filter_product, name="filter-product"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("cart/", cart_view, name="cart"),
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    path("update-cart/", update_cart, name="update-cart"),





]