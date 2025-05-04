from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Category, Product
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.core.cache import cache
from catalog.services import get_products_by_category


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


class CategoryCreateView(CreateView):
    model = Category
    fields = ("name", "description", "image")
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ("name", "description", "image")
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(DetailView):
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:category_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        key = 'all_products'
        products = cache.get(key)
        if products is None:
            products = list(Product.objects.filter(status=True).select_related('category'))
            cache.set(key, products, 60 * 15)
        return products


@method_decorator(cache_page(60*15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        return self.get_object().owner == self.request.user



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        user = self.request.user
        product = self.get_object()
        return (product.owner == user) or user.has_perm('products.delete_product')


class ProductsByCategoryView(ListView):
    model = Product
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'


    def get_queryset(self):
        return get_products_by_category(self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return ctx

@login_required
@permission_required('products.can_unpublish_product', raise_exception=True)
def unpublish_product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    prod.status = False
    prod.save()
    return redirect('products:detail', pk=pk)
