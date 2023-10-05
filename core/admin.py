from django.contrib import admin

from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Adress

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ["user", "title", "product_image","category", "featured", "product_status", "pid"]

# class Sub_ProductImagesAdmin(admin.TabularInline):
#     model = Sub_ProductImages

# class Sub_ProductAdmin(admin.ModelAdmin):
#     inlines = [Sub_ProductImagesAdmin]
#     list_display = ["user", "title", "product_image", "category", "featured", "product_status", "spid"]





class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]


class VendorAdmin(admin.ModelAdmin):
    list_display = ["title", "vendor_image"]


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "paid_status", "order_date", "product_status"]


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["order", "invoice_no", "item", "image", "price", "total"]


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]


class WishlistReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "date"]


class AdressAdmin(admin.ModelAdmin):
    list_display = ["user", "adress", "status"]




admin.site.register(Product, ProductAdmin)
# admin.site.register(Sub_Product, Sub_ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistReviewAdmin)
admin.site.register(Adress, AdressAdmin)








