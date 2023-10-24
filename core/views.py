from django.shortcuts import render, get_object_or_404, redirect
from django.http import  JsonResponse
from taggit.models import Tag
from core.models import *
from userauths.models import *
from django.contrib import messages
from django.db.models import Avg
from core.forms import *
from userauths.forms import *
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required









def index(request):
    # product = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status= "published",featured = True)
    category = Category.objects.all()
    categorynav = Category.objects.all()
    

    if request.method == "POST":
        
        about = request.POST["aboutjoboffer"]
        email = request.POST["emailjoboffer"]
        


        new_job = JobOffer.objects.create(
            
            about=about,
            email=email,
            
        )
        new_job.save()
        messages.success(request, "باتشکر")
        return redirect("core:index")
    else:
        print("error")


    context = {
        "products": products,
        "categories": category,
        "categorynav": categorynav,

    }
    return render(request, 'core/index.html', context)




def blank(request):
    
    categorynav = Category.objects.all()
    context = {
        
        "categorynav": categorynav,

    }
    return render(request, 'core/blank.html', context)




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
    vendors = request.GET.getlist("Vendor[]")
    typecategory = request.GET.getlist("typecategory[]")
    sizecategory = request.GET.getlist("sizecategory[]")
    tagcategory = request.GET.getlist("tagcategory[]")
    colorcategory = request.GET.getlist("colorcategory[]")
    languagecategory = request.GET.getlist("languagecategory[]")
    # و بقیه فبتر ها مانند وندور
    products = Product.objects.filter(product_status="published").order_by("-id").distinct()

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()

    if len(vendors) > 0:
        products = products.filter(Vendor__id__in=vendors).distinct()

    if len(typecategory) > 0:
        products = products.filter(typecategory__id__in=typecategory).distinct()
    if len(sizecategory) > 0:
        products = products.filter(sizecategory__id__in=sizecategory).distinct()
    if len(tagcategory) > 0:
        products = products.filter(tagcategory__id__in=tagcategory).distinct()
    if len(colorcategory) > 0:
        products = products.filter(colorcategory__id__in=colorcategory).distinct()
    if len(languagecategory) > 0:
        products = products.filter(languagecategory__id__in=languagecategory).distinct()


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
            cart_total_amount += int(item['qty']) * int(item['price'])
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
            cart_total_amount += int(item['qty']) * int(item['price'])

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
            cart_total_amount += int(item['qty']) * int(item['price'])

    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})



@login_required
def checkout_view(request):
    adress = Adress.objects.filter(user=request.user)

    cart_total_amount = 0
    total_amount = 0
    # checking if cart_data_obj session exist
    if 'cart_data_obj' in request.session:

        # getting total amount for the payment
        for p_id, item in request.session['cart_data_obj'].items():
            total_amount += int(item['qty']) * int(item['price'])
        # creating order object
        order = CartOrder.objects.create(
            user=request.user,
            price = total_amount,

        )
        # getting total amount for the cart
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * int(item['price'])

            cart_order_products = CartOrderItems.objects.create(
                order=order,
                invoice_no="INVOICE_NO-"+str(order.id),
                item=item['title'],
                image=item['image'],
                qty=item['qty'],
                price=item['price'],
                total=int(item['qty']) * int(item['price']),

            )


    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * int(item['price'])


        # try:
        #     active_adress = Adress.objects.get(user=request.user, status= True)
        # except:
        #     messages.warning(request, "there are multiple adresss, only one should be active. select from dashboard")
        #     active_adress+ None
        return render(request, "core/checkout.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount, 'adress':adress })



@login_required
def checkout_information_view(request):
    orders = CartOrder.objects.filter(user=request.user).order_by("-id")
    adressfield = Adress.objects.filter(user=request.user)
    
    


    if request.method == "POST":
        user = request.user
        checkoutadress = request.POST["checkoutadress"]
        mobile = request.POST["checkoutmobile"]
        firstname = request.POST["checkoutfirstname"]
        lastname = request.POST["checkoutlastname"]
        postcode = request.POST["checkoutpostcode"]
        stateadress = request.POST["checkoutstateadress"]
        city = request.POST["checkoutcity"]


        new_adress = Adress.objects.create(
            
            adress=checkoutadress,
            mobile=mobile,
            firstname=firstname,
            lastname=lastname,
            postcode=postcode,
            stateadress=stateadress,
            city=city,
            user=user,
        )
        new_adress.save()
        messages.success(request, ".ادرس با موفقیت اضافه شد")
        return redirect("core:checkout")
    else:
        print("error")
    # user_profile = Profile.objects.get(user=request.user)
    context = {
        "orders": orders,
        "adressfield": adressfield,
        # "user_profile": user_profile,
        
        


    }

    return render(request, 'core/checkout-information.html', context)



def payment_compeleted_view(request):
    return render(request, 'core/payment-compeleted.thml')



def payment_failed_view(request):
    return render(request, 'core/payment-failed.thml')



@login_required
def customer_dashboard(request):
    orders = CartOrder.objects.filter(user=request.user).order_by("-id")
    adress = Adress.objects.filter(user=request.user)
    
    
    

    if request.method == "POST":
        adress = request.POST.get("adress")
        mobile = request.POST.get("mobile")

        new_adress = Adress.objects.update(
            user=request.user,
            adress=adress,
            mobile=mobile,

        )
        messages.success(request, ".ادرس با موفقیت اضافه شد")
        return redirect("core:dashboard")
    else:
        print("error")
    # user_profile = Profile.objects.get(user=request.user)



    



    context = {
        "orders": orders,
        "adress": adress,
        # "user_profile": user_profile,
       
        
        


    }


    return render(request, "core/dashboard.html", context)



@login_required
def order_detail(request, id):
    order = CartOrder.objects.get(user=request.user, id=id)
    products = CartOrderItems.objects.filter(order=order)
    context = {
        "products": products
    }
    return render(request, "core/orderdetail.html", context)



def make_adress_default(request):
    id = request.GET["id"]
    Adress.objects.update(status=False)
    Adress.objects.filter(id=id).update(status=True)
    return JsonResponse({"boolean": True})



@login_required
def contact_view(request):
    return render(request, "core/contact.html")



@login_required
def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        full_name = full_name,
        email = email,
        phone = phone,
        subject = subject,
        message = message,
    )
    data = {
        "bool": True,
        "message": ".نظر با موفقیت ارساب شد"
    }
    return JsonResponse({"data":data})