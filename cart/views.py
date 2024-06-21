from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from profi_main.models import Product
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm
from .models import OrderItem, Order
from django.contrib.auth.decorators import login_required

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
             quantity=1,  # Здесь задаем количество явно равным 1
             update_quantity=cd['update'])
        print("Product added to cart:", product_id, "Quantity:", 1)  # Выводим количество 1
    else:
        print("Form is not valid:", form.errors)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'])
            # очистка корзины
            cart.clear()
            return redirect('profi_main:index')
    else:
        form = OrderCreateForm
    return render(request, 'market/order.html',
                  {'cart': cart, 'form': form})



@login_required
def my_courses(request):
    orders = Order.objects.filter(email=request.user.email, paid=True)
    
    courses = []
    for order in orders:
        for item in order.items.all():
            courses.append(item.product)
    
    context = {
        'courses': courses
    }
    return render(request, 'market/my_courses.html', context)




