from .models import Product

def get_products_by_category(slug):
    return Product.objects.filter(
        category__slug=slug,
        status=True
    ).select_related('category').order_by('name')
