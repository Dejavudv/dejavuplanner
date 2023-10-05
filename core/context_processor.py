from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Adress



def default(request):
    categories = Category.objects.all()
    try:
        adress = Adress.objects.get(user=request.user)

    except:
        adress = None

    return {
        'categories' : categories,
    }