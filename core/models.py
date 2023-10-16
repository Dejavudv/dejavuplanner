from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField






STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),

)


STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("regected", "Rejected"),
    ("in_review", "In_review"),
    ("published", "Published"),

)


RATING = (
    (1 , "★☆☆☆☆"),
    (2 , "★★☆☆☆"),
    (3 , "★★★☆☆"),
    (4 , "★★★★☆"),
    (5 , "★★★★★"),

)



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)







class Category(models.Model):
    cid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="planner")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class tags(models.Model):
    pass

    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "ven", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="dv")
    image = models.ImageField(upload_to = user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default="i'm a amazing vendor")

    adress = models.CharField(max_length=100, default="123 main street, london")
    contact = models.CharField(max_length=100, default="09***")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shiping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warrantty_period = models.CharField(max_length=100, default="100")



    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    



##############################  sub product    ################################

# class Sub_Product(models.Model):
#     spid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "sprd", alphabet = "abcdefgh12345")

#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="subcategory")
#     Vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
#     # product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="subproduct")   
#     title = models.CharField(max_length=100, default="fresh pear")
#     image = models.ImageField(upload_to = user_directory_path, default="product.jpg")
#     description = models.TextField(null=True, blank=True, default="this is the product")
#     more_description = models.TextField(null=True, blank=True, default="this is more product")
#     information = models.TextField(null=True, blank=True, default="this is the information part")


#     price = models.DecimalField(max_digits=999999999999999999, decimal_places=3, default="100,000")
#     old_price = models.DecimalField(max_digits=999999999999999999, decimal_places=3, default="200,000")

#     specifications = models.TextField(null=True, blank=True, default="")
#     # tags = models.ForeignKey(tags, on_delete=models.SET_NULL, null=True)
#     product_status = models.CharField(choices= STATUS, max_length=10, default="in_review")

#     status = models.BooleanField(default=True)
#     in_stock = models.BooleanField(default=True)
#     featured = models.BooleanField(default= False)
#     digital = models.BooleanField(default= False)

#     sku = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "sku", alphabet = "1234567890")

#     date = models.TimeField(auto_now_add=True)
#     updated = models.TimeField(null=True, blank=True)

#     class Meta:
#         verbose_name_plural = " sub products"

#     def product_image(self):
#         return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
#     def __str__(self):
#         return self.title
    
#     def get_precentage(self):
#         # new_price = (self.price / self.old_price) * 100
#         new_price = (((self.old_price - self.price)*100)/self.old_price)
#         return new_price
    




# class Sub_ProductImages(models.Model):
#     images = models.ImageField(upload_to="Sub_product_images", default="product.jpg")
#     subproduct = models.ForeignKey(Sub_Product ,on_delete=models.SET_NULL, null=True)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Sub Product Images"
    
######################################
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "prd", alphabet = "abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    Vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    # sub_product = models.ForeignKey(Sub_Product, on_delete=models.SET_NULL, null=True)
    # products = models.ManyToManyField(Sub_Product)

    title = models.CharField(max_length=100, default="fresh pear")
    image = models.ImageField(upload_to = user_directory_path, default="product.jpg")
    # description = models.TextField(null=True, blank=True, default="this is the product")
    # more_description = models.TextField(null=True, blank=True, default="this is more product")
    # information = models.TextField(null=True, blank=True, default="this is the information part")
    description = RichTextUploadingField(null=True, blank=True, default="this is the product")
    more_description = RichTextUploadingField(null=True, blank=True, default="this is more product")
    information = RichTextUploadingField(null=True, blank=True, default="this is the information part")

    price = models.DecimalField(max_digits=999999999999999999, decimal_places=3, default="100,000")
    old_price = models.DecimalField(max_digits=999999999999999999, decimal_places=3, default="200,000")

    specifications = models.TextField(null=True, blank=True, default="")
    tags = TaggableManager(blank=True)
    product_status = models.CharField(choices= STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default= False)
    digital = models.BooleanField(default= False)

    sku = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "sku", alphabet = "1234567890")

    date = models.TimeField(auto_now_add=True)
    updated = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "products"

    def product_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_precentage(self):
        # new_price = (self.price / self.old_price) * 100
        new_price = (((self.old_price - self.price)*100)/self.old_price)
        return new_price
    



class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="p_images" ,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"















####################cart, order, orderitems and adress###################
####################cart, order, orderitems and adress###################
####################cart, order, orderitems and adress###################
####################cart, order, orderitems and adress###################



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="100,000")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices= STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = "Cart Order"




class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete= models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0 )
    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="100,000")
    total = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default="100,000")


    class Meta:
        verbose_name_plural = "Cart Order Items"
        
    def order_img(self):
        return mark_safe('<img src = "/media/%s"  width = "50" height="50" />' % (self.image))
    

###########################product review whishlist adress########################################
###########################product review whishlist adress########################################
###########################product review whishlist adress########################################
###########################product review whishlist adress########################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default= 5)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "product Reviews"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    


class Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=100, null= True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "adress"




















































