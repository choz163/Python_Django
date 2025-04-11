from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path ('base/', CategoryListView.as_view(), name='category_list'),
    path ('category/<int:pk>', CategoryDetailView.as_view(), name='category_list'),
    path ('catalog/create/', CategoryCreateView.as_view(), name='category_create'),
    path ('catalog/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path ('catalog/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
