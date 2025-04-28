from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', RedirectView.as_view(url='blog/base', permanent=False)),
    path('', include('catalog.urls', namespace="catalog")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('users/', include('users.urls', namespace='users')),
]
