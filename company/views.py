from django.shortcuts import render
from shop.models import Product
from cart.models import Orders, OrdersItem
from datetime import datetime

def mainPage(request):
    context = {}
    current_user = request.user
    if (current_user.activity == 'company'):
        return render(request, 'company/main.html', context)
    else:
        return render(request, 'company/not_loggined.html')

def ordersPage(request):
    order_list = []
    brand_id = 23
    order = OrdersItem.objects.filter(brand=brand_id)
    for o in order:
        get_order = Orders.objects.get(id=o.order_id)
        get_product = Product.objects.get(id=o.product_id)
        created = datetime.strftime(get_order.created, "%Y-%m-%d %H:%M")
        updated = datetime.strftime(get_order.updated, "%Y-%m-%d %H:%M")
        data = {
            'name': get_order.name,
            'telephone': get_order.telephone,
            'city': get_order.city,
            'address': get_order.address,
            'created': created,
            'updated': updated,
            'product': get_product.name,
            'quantity': o.quantity,
            'price': get_product.price
        }
        order_list.append(data)
    context = {
        'orders': order_list
    }
    return render(request, 'company/orders.html', context)

def productsPage(request):
    context = {}
    product = Product.objects.filter(brand_id=23)
    print(product)
    return render(request, 'company/products.html', context)

def staffPage(request):
    context = {}
    return render(request, 'company/staff.html', context)

def statPage(request):
    context = {}
    return render(request, 'company/stat.html', context)
    
