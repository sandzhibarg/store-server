from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(extra_context={'title': 'Store'}), name='index'),
    path('products/', include('products.urls', namespace='products')), # перенаправка на файл urls.py приложения products
    path('users/', include('users.urls', namespace='users')), # перенаправка на файл urls.py приложения users
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
