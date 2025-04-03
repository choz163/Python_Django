from catalog.models import Category, Product
from django.shortcuts import render, get_object_or_404

def home(request):
    categories = Category.objects.all()  # Получаем все категории
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'home.html', {'category': Category, 'products': products})

def contacts(request):
    return render(request, 'contacts.html')

def category_list(request):
    category= Category.objects.all()
    context = {"category": category}
    return render(request, 'category_list.html', context)

def product_list(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_list.html', context)