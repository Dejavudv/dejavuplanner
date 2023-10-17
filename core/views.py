from django.shortcuts import render, get_object_or_404, redirect
from django.http import  JsonResponse
from taggit.models import Tag
from core.models import *
from django.contrib import messages
from django.db.models import Avg
from core.forms import ProductReviewForm
from django.template.loader import render_to_string
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

    make_review = True
    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user = request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    context = {
        "product": product,
        "make_review": make_review,
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



def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "products": products,
        "query": query,
    }

    return render(request, "core/search.html", context)


def filter_product(request):
    categories = request.GET.getlist("category[]")
    # vendors = request.GET.getlist("vendor[]")
    # و بقیه فبتر ها مانند وندور
    products = Product.objects.filter(product_status="published").order_by("-id").distinct()

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()

    # if len(vendors) > 0:
    #     products = products.filter(vendor__id__in=vendors).distinct()

    data = render_to_string("core/async/product-list.html",{"products": products})
    return JsonResponse({"data":data})



def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],

    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data

        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data

    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})





def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "core/cart.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    else:
        messages.warning(request, "your cart is empty")
        return redirect("core:index")
    
def delete_item_from_cart(request):
    product_id = str(request.GET["id"]) 
    if "cart_data_obj" in request.session:
        if product_id in request.session["cart_data_obj"]:
            cart_data = request.session["cart_data_obj"]
            del request.session["cart_data_obj"][product_id]
            request.session["cart_data_obj"] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})

def update_cart(request):
    product_id = str(request.GET["id"]) 
    product_qty = request.GET["qty"]
    if "cart_data_obj" in request.session:
        if product_id in request.session["cart_data_obj"]:
            cart_data = request.session["cart_data_obj"]
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session["cart_data_obj"] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})


















