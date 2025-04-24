from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name


urlpatterns = [
    path ('base', CategoryListView.as_view(), name='category_list'),
    path ('category/<int:pk>', CategoryDetailView.as_view(), name='category_list'),
    path ('catalog/create/', CategoryCreateView.as_view(), name='category_create'),
    path ('catalog/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path ('catalog/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
