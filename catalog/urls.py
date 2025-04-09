from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, category_list, product_list

app_name = CatalogConfig.name


urlpatterns = [
    path ('contacts', contacts, name='contacts'),
    path ('base', category_list, name='category_list'),
    path ('product/<int:pk>', product_list, name='product_list')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
