from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm
from .models import OrdersItem
from django.contrib import auth


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
    total_sum = 0
    for item in cart:
        total_sum += item['total_price']
    current_user = request.user
    user_id = current_user.id
    print(user_id)
    fName = current_user.first_name
    tel = current_user.telephone
    address = current_user.address
    city = current_user.city
    activity = current_user.activity
    if request.method == 'POST':
        print('here')
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            for item in cart:
                order = form.save()
                OrdersItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return redirect('order/')
    else:
        print('error')
    context = {
        'cart': cart,
        'total': total_sum,
        'name': fName,
        'telephone': tel,
        'address': address,
        'city': city,
        'activity': activity
    }
    return render(request, 'cart/detail.html', context)

def order_created(request):
    return render(request, 'cart/order.html')