import random
from django.shortcuts import render
from .models import Category, Brand, Product
from cart.forms import CartAddProductForm

def shopPage(request, category_slug=None):
    context = {}
    categories = Category.objects.all()
    products = sorted(Product.objects.all(), key=lambda x: random.random())
    context['products'] = products
    context['categories'] = categories
    print(request.path)
    return render(request, 'shop/shop.html', context)

def shopMain(request):
    context = {}
    return render(request, 'shop/main.html', context)

def brand_list(request, slug):
    context = {}
    category = Category.objects.get(slug=slug)
    brands = Brand.objects.filter(category=category)
    context['category'] = category
    brand_arr = []
    product_all = []
    for brand in brands:
        product_len = len(Product.objects.filter(brand=brand))
        b = {
            'name': brand.name,
            'slug': brand.slug,
            'products_len': product_len
        }
        brand_arr.append(b)
        for prod in Product.objects.filter(brand=brand):
            product_all.append(prod)
    context['brands'] = brand_arr
    context['product_all'] = product_all
    return render(request, 'shop/list.html', context)

def products_list(request, slug):
    context = {}
    brand = Brand.objects.get(slug=slug)
    products = Product.objects.filter(brand=brand)
    context['products'] = products
    context['brand'] = brand
    return render(request, 'shop/products.html', context)

def product_detail(request, id):
    context = {}
    product = Product.objects.get(id=id)
    context['product'] = product
    context['cart_product_form'] = CartAddProductForm(initial={'quantity': product.min_order})
    return render(request, 'shop/detail.html', context)