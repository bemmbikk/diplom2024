from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Category,Teacher
from cart.forms import CartAddProductForm
from django.contrib import messages
from .forms import ContactForm
from authorization.forms import UserRegisterForm
import logging

logger = logging.getLogger(__name__)
    
def index(request):
    contact_form = ContactForm(prefix='contact')
    if request.method == 'POST':
        if 'contact' in request.POST:
            contact_form = ContactForm(request.POST, prefix='contact')
            
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Форма обратной связи успешно отправлена!')
                return redirect('profi_main:index')
            else:
                logger.error(f'Ошибка валидации формы обратной связи: {contact_form.errors}')
                messages.error(request, 'Произошла ошибка при отправке формы обратной связи. Пожалуйста, попробуйте снова.')
    return render(request, 'main/index.html', {
        'contact_form': contact_form,
    })


def contacts(request):
    return render(request,'main/contacts.html')

def about(request):
    category = None
    teachers = Teacher.objects.all()
    return render(request,
                  'main/about_us.html',
                  {'teachers': teachers})

def product_list(request, category_slug=None):
    category = None
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'market/list.html',
                  {'category': category,
                  'cart_product_form': cart_product_form,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'market/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        
    })

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, prefix='contact')

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Форма обратной связи успешно отправлена!')
            return redirect('profi_main:index')
        else:
            logger.error(f'Ошибка валидации формы обратной связи: {contact_form.errors}')
            messages.error(request, 'Произошла ошибка при отправке формы обратной связи. Пожалуйста, попробуйте снова.')
    else:
        contact_form = ContactForm(prefix='contact')

    return render(request, 'main/index.html', {
        'form': contact_form,
    })

