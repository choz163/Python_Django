from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.models import Category, Product


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_list.html'
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