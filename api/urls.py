from django.conf.urls import include, url

from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'color', ShoeColorViewSet, basename='color_name')
router.register(r'type', ShoeTypeViewSet, basename='type')
router.register(r'shoe', ShoeViewSet, basename='shoe')

urlpatterns = [
    url(r"^api/", include(router.urls))
]