from django.contrib import admin

from core.models import *

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
    list_display = ["title", "category_image", "id"]

class typeCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
class sizeCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
class tagCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
class colorCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "colorcategory_image"]
class languageCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


class VendorAdmin(admin.ModelAdmin):
    list_display = ["title"]


class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ["paid_status", "product_status"]
    list_display = ["user", "price", "paid_status", "order_date", "product_status"]


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ["order", "invoice_no", "item", "image", "price", "total"]


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]


class WishlistReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "date"]


class AdressAdmin(admin.ModelAdmin):
    list_editable = ["adress", "status"]
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
admin.site.register(typeCategory, typeCategoryAdmin)
admin.site.register(sizeCategory, sizeCategoryAdmin)
admin.site.register(tagCategory, tagCategoryAdmin)
admin.site.register(colorCategory, colorCategoryAdmin)
admin.site.register(languageCategory, languageCategoryAdmin)







