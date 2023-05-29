from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
