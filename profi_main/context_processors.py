from .models import Category, Product
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def categories(request):
    return {'categories': Category.objects.all()}

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return {  'products': products }

from .forms import ContactForm

def contact_form(request):
    return {
        'contact_form': ContactForm(prefix='contact')
    }
