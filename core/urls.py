from django.urls import path
from core.views import *

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
    path("checkout/", checkout_view, name="checkout"),
    path("dashboard/", customer_dashboard, name="dashboard"),
    path("payment-compeleted/", payment_compeleted_view, name="payment-compeleted"),
    path("payment-failed/", payment_failed_view, name="payment-failed"),
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),
    path("make-default-adress/", make_adress_default, name="make-default-adress"),
    path("contact/", contact_view, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),


    path("checkout-information/", checkout_information_view, name="checkout-information"),




    




]