from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from taggit.models import Tag
from core.models import *
from math import prod
from django.db.models import Avg
from core.forms import ProductReviewForm
from stripe import review
# Create your views here.
def index(request):
    # product = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status= "published",featured = True)
    category = Category.objects.all()
    context = {
        "products": products,
        "categories": category,
    }
    return render(request, 'core/index.html', context)



def blank(request):

    return render(request, 'core/blank.html')



def product_list_view(request):
    products = Product.objects.filter(product_status= "published")

    context = {
        "products": products
    }
    return render(request, 'core/product-list.html', context)



def category_list_view(request):
    category = Category.objects.all()
    context = {
        "categories": category
    }
    return render(request, 'core/category-list.html', context)



def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status= "published", category=category)
    context = {
        "category": category,
        "products": products,
    }
    return render(request, 'core/category-product-list.html', context)



def custom_product_list(request):

    products = Product.objects.filter(product_status= "published")
    context = {
        "products": products,
    }
    return render(request, 'core/custom.html', context)



def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)

    # product = get_object_or_404(Product, pid=pid)
    p_image = product.p_images.all()
    
    products = Product.objects.filter(category=product.category).exclude(pid=pid)


    
    # creating reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")
    # getting average review
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating = Avg('rating'))
    # product review form 
    review_form = ProductReviewForm()


    context = {
        "product": product,
        "p_image": p_image,
        "products": products,
        "reviews": reviews,
        "average_rating": average_rating,
        "review_form": review_form,

    }

    return render(request, "core/product-detail.html", context)



def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status = "published").order_by("-id")


    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])


    context = {
        "products": products,
        "tag": tag,
    }
    return render(request, "core/tag.html", context)


def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user
    review = ProductReview.objects.create(
        user = user,
        product = product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )



    context = {
        "user": user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],


    }
    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))


    return JsonResponse(
        {
        'bool': True,
        'context': context,
        'average_reviews': average_reviews,
        }
    )



