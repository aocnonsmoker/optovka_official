from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    for item in cart:
        if item['product'] == product:
            item['quantity'] += 1
            cart.augment_quantity(quantity=item['quantity'], product_id=product_id)            
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    if request.POST:
        product_id = request.POST.get('product_plus')
        product = get_object_or_404(Product, id=product_id)
        for item in cart:
            if item['product'] == product:
                item['quantity'] += 1
                cart.add(product=product,
                         quantity=item['quantity'],
                         update_quantity=False)
                print('success')
    return render(request, 'cart/detail.html', {'cart': cart})