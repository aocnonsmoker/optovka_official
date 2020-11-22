from django.shortcuts import render
from .models import Category, Brand, Product
from cart.forms import CartAddProductForm

def shopPage(request, category_slug=None):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request, 'shop/shop.html', context)

def shopMain(request):
    context = {}
    return render(request, 'shop/main.html', context)

def brand_list(request, slug):
    context = {}
    category = Category.objects.get(slug=slug)
    brands = Brand.objects.filter(category=category)
    context['category'] = category
    context['brands'] = brands
    return render(request, 'shop/list.html', context)

def products_list(request, slug):
    context = {}
    brand = Brand.objects.get(slug=slug)
    products = Product.objects.filter(brand=brand)
    context['products'] = products
    return render(request, 'shop/products.html', context)

def product_detail(request, id):
    context = {}
    product = Product.objects.get(id=id)
    context['product'] = product
    context['cart_product_form'] = CartAddProductForm()
    return render(request, 'shop/detail.html', context)