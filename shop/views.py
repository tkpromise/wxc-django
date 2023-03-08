from django.shortcuts import render, get_object_or_404

from django.core import serializers
from django.http import JsonResponse, HttpResponse

from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request, category_slug=None):
    res = request.META.get('X-WX-OPENID')
    res2 = request.META.get('REMOTE_HOST')
     
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        prodcuts = products.filter(category=category)
    # return render(request, 'shop/product/list2.html', {'category': categories, 'products': products, 'user_agent': user_agent, 'u2':u2})
    # return render(request, 'shop/product/list2.html', 
                  # {'user_agent': user_agent, 'u2':u2})
    # data = serializers.serialize('json', user_agent)
    # return JsonResponse(user_agent)
    # return HttpResponse({'user_agent': user_agent}, content_type='application/json')
    return HttpResponse(res )

    


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
