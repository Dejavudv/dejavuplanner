from core.models import *



def default(request):
    categories = Category.objects.all().exclude(id=6)
    typecategory = typeCategory.objects.all()
    sizecategory = sizeCategory.objects.all()
    tagcategory = tagCategory.objects.all()
    colorcategory = colorCategory.objects.all()
    languagecategory = languageCategory.objects.all()
    categorynav = Category.objects.all()

    vendors = Vendor.objects.all()
    try:
        adress = Adress.objects.get(user=request.user)

    except:
        adress = None

    return {
        'categories' : categories,
        'categorynav' : categorynav,
        'vendors' : vendors,
        'typecategory': typecategory,
        'sizecategory': sizecategory,
        'tagcategory': tagcategory,
        'colorcategory': colorcategory,
        'languagecategory': languagecategory,

    }