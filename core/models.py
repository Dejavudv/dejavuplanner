from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField






STATUS_CHOICE = (
    ("processing", "Processing"),
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


# ####################################################


class typeCategory(models.Model):
    typecid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="planner")
    image = models.ImageField(upload_to="typecategory", default="category.jpg", blank=True, null=True)

    class Meta:
        verbose_name_plural = "typeCategories"

    def typecategory_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class sizeCategory(models.Model):
    sizecid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="planner")
    image = models.ImageField(upload_to="sizecategory", default="category.jpg" , blank=True, null=True)

    class Meta:
        verbose_name_plural = "sizeCategories"

    def sizecategory_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class tagCategory(models.Model):
    tagcid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="planner")
    image = models.ImageField(upload_to="tagcategory", default="category.jpg" , blank=True, null=True)

    class Meta:
        verbose_name_plural = "tagCategories"

    def tagcategory_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class colorCategory(models.Model):
    colorcid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="planner")
    image = models.ImageField(upload_to="colorcategory", default="category.jpg" , blank=True, null=True)

    class Meta:
        verbose_name_plural = "colorCategories"

    def colorcategory_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class languageCategory(models.Model):
    languagecid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "cat", alphabet = "abcdefgh12345")
    title = models.CharField(max_length=100, default="planner")
    image = models.ImageField(upload_to="languagecategory", default="category.jpg" , blank=True, null=True)

    class Meta:
        verbose_name_plural = "languageCategories"

    def languagecategory_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title



    
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
    



# ----------------------------------------------------
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length= 10, max_length = 30, prefix= "prd", alphabet = "abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    Vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    typecategory = models.ForeignKey(typeCategory, on_delete=models.SET_NULL, null=True, related_name="typecategory")
    sizecategory = models.ForeignKey(sizeCategory, on_delete=models.SET_NULL, null=True, related_name="sizecategory")
    tagcategory = models.ForeignKey(tagCategory, on_delete=models.SET_NULL, null=True, related_name="tagcategory")
    colorcategory = models.ForeignKey(colorCategory, on_delete=models.SET_NULL, null=True, related_name="colorcategory")
    languagecategory = models.ForeignKey(languageCategory, on_delete=models.SET_NULL, null=True, related_name="languagecategory")

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

    price = models.IntegerField()
    old_price = models.IntegerField()

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

class Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=100, null= True)
    mobile = models.CharField(max_length=100, null= True)

    firstname = models.CharField(max_length=100, null= True)
    lastname = models.CharField(max_length=100, null= True)
    postcode = models.CharField(max_length=100, null= True)
    stateadress = models.CharField(max_length=100, null= True)
    city = models.CharField(max_length=100, null= True)

    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "adress"

    def __str__(self):
        return self.postcode







class CartOrder(models.Model):
    
    adress = models.ForeignKey(Adress, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    price = models.IntegerField()
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
    image = models.ImageField(upload_to="cartorderitems", default="category.jpg" , blank=True, null=True)
    qty = models.IntegerField(default=0 )
    price = models.IntegerField()
    total = models.IntegerField()


    class Meta:
        verbose_name_plural = "Cart Order Items"

    def cartorderitems_image(self):
        return mark_safe('<img src = "%s"  width = "50" height="50" />' % (self.image.url))
    
        
    # def order_img(self):
        # return mark_safe('<img src = "/media/%s"  width = "50" height="50" />' % (self.image))
    

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
    

















































